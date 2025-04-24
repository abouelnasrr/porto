from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactMessageForm, PortoForm, ProjectForm, ProjectMediaForm
from .models import ContactMessage, PortoData, Project, ProjectMedia
from .models import Experience, Education
from .forms import ExperienceForm, EducationForm
from .models import Language, Volunteering, Skill
from .forms import LanguageForm, VolunteeringForm, SkillForm
from .models import YouTubeIntro, YouTubeVideo
from .forms import YouTubeIntroForm, YouTubeVideoForm
from .models import DashboardSecurity
from .forms import DashboardSecurityForm

def porto(request):
    # Get the latest PortoData or use defaults
    porto_data = PortoData.objects.last()
    form = ContactMessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('porto')

    if porto_data and porto_data.photo:
        name = porto_data.name or "No Name"
        title = porto_data.title or "No Title"
        photo_url = porto_data.photo.url if porto_data.photo else 'images/photo_not_found.jpg'
        is_uploaded_photo = True

    else:
        name = "No Name"
        title = "No Title"
        photo_url = 'images/photo_not_found.jpg'
        is_uploaded_photo = False

    name = porto_data.name if porto_data and porto_data.name else "No Name"
    title = porto_data.title if porto_data and porto_data.title else "No Title"
    projects = Project.objects.prefetch_related('media').all()

    return render(request, 'main/porto.html', {
        'name': name,
        'form': form,
        'projects': projects,
        'title': title,
        'photo_url': photo_url,
        'is_uploaded_photo': is_uploaded_photo
    })

def dashboard(request):
    if not request.session.get('step3_passed'):
        return redirect('auth_login')

    youtube_intro, _ = YouTubeIntro.objects.get_or_create(pk=1)
    youtube_intro_form = YouTubeIntroForm(request.POST or None, instance=youtube_intro)
    youtube_video_form = YouTubeVideoForm()
    youtube_videos = YouTubeVideo.objects.all()
    language_form = LanguageForm()
    languages = Language.objects.all()

    volunteering_form = VolunteeringForm()
    volunteerings = Volunteering.objects.all()
    security, _ = DashboardSecurity.objects.get_or_create(pk=1)
    security_form = DashboardSecurityForm(request.POST or None, instance=security)

    skill_form = SkillForm()
    skills = Skill.objects.all()
    education_form = EducationForm()
    educations = Education.objects.all()
    experience_form = ExperienceForm()
    experiences = Experience.objects.all()
    project_form = ProjectForm()
    media_form = ProjectMediaForm()
    projects = Project.objects.all()
    from django.utils import timezone
    from datetime import timedelta
    messages = ContactMessage.objects.filter(is_saved=False, is_starred=False)
    starred = ContactMessage.objects.filter(is_starred=True)
    saved = ContactMessage.objects.filter(is_saved=True)
    porto_data = PortoData.objects.last()
    name = porto_data.name if porto_data and porto_data.name else "No Name"
    title = porto_data.title if porto_data and porto_data.title else "No Title"
    photo_url = porto_data.photo.url if porto_data and porto_data.photo else 'images/photo_not_found.jpg'
    is_uploaded_photo = bool(porto_data and porto_data.photo)
    summary = PortoData.objects.last().summary if PortoData.objects.last() else "No summary available."

    ContactMessage.objects.filter(
        is_saved=False,
        is_starred=False,
        timestamp__lt=timezone.now() - timedelta(days=30)
    ).delete()
    
    if request.method == 'POST' and 'save_security' in request.POST:
        if security_form.is_valid():
            security_form.save()
            return redirect('dashboard')

    if request.method == 'POST':
        if 'save_intro' in request.POST and youtube_intro_form.is_valid():
            youtube_intro_form.save()
            return redirect('dashboard')

        if 'add_video' in request.POST:
            youtube_video_form = YouTubeVideoForm(request.POST)
            if youtube_video_form.is_valid():
                youtube_video_form.save()
                return redirect('dashboard')
        if 'language_submit' in request.POST:
            language_form = LanguageForm(request.POST)
            if language_form.is_valid():
                language_form.save()
                return redirect('dashboard')
        elif 'volunteering_submit' in request.POST:
            volunteering_form = VolunteeringForm(request.POST)
            if volunteering_form.is_valid():
                volunteering_form.save()
                return redirect('dashboard')
        elif 'skill_submit' in request.POST:
            skill_form = SkillForm(request.POST)
            if skill_form.is_valid():
                skill_form.save()
                return redirect('dashboard')
        
    if request.method == 'POST' and 'education_submit' in request.POST:
        education_form = EducationForm(request.POST)
        if education_form.is_valid():
            education_form.save()
            return redirect('dashboard')

    if request.method == 'POST' and 'experience_submit' in request.POST:
        experience_form = ExperienceForm(request.POST)
        if experience_form.is_valid():
            experience_form.save()
            return redirect('dashboard')
    if request.method == 'POST' and 'summary' in request.POST:
        if porto_data:
            porto_data.summary = request.POST.get('summary')
            porto_data.save()
        return redirect('dashboard')
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        media_files = request.FILES.getlist('file')  # Get all files uploaded under the 'file' field
        form = PortoForm(request.POST, request.FILES)
        
        if project_form.is_valid():
            # Save the project
            project = project_form.save()

            # Save each media file as a ProjectMedia object
            for f in media_files:
                ProjectMedia.objects.create(project=project, file=f)

            return redirect('dashboard')

        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to Porto page after save
    else:
        form = PortoForm()
    return render(request, 'main/dashboard.html', {
        'summary': porto_data.summary if porto_data else "",
        'porto_data': porto_data,
        'form': form,
        'project_form': project_form,
        'media_form': media_form,
        'projects': projects,
        'messages': messages,
        'starred': starred,
        'saved': saved,
        'summary': summary,
        'name': name,
        'title': title,
        'photo_url': photo_url,
        'is_uploaded_photo': is_uploaded_photo,
        'experience_form': experience_form,
        'experiences': experiences,
        'education_form': education_form,
        'educations': educations,
        'language_form': language_form,
        'languages': languages,
        'volunteering_form': volunteering_form,
        'volunteerings': volunteerings,
        'skill_form': skill_form,
        'skills': skills,
        'youtube_intro_form': youtube_intro_form,
        'youtube_video_form': youtube_video_form,
        'youtube_videos': youtube_videos,
        'security_form': security_form,

    })



def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('dashboard')

def save_message(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_saved = True
    msg.save()
    return redirect('dashboard')

def star_message(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_starred = True
    msg.save()
    return redirect('dashboard')

def delete_message(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    return redirect('dashboard')


def cv(request):
    from .models import PortoData
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    languages = Language.objects.all()
    volunteerings = Volunteering.objects.all()
    skills = Skill.objects.all()


    summary = PortoData.objects.last().summary if PortoData.objects.last() else "No summary available."
    return render(request, 'main/cv.html', {
        'summary': summary,
        'experiences': experiences,
        'educations': educations,
        'languages': languages,
        'volunteerings': volunteerings,
        'skills': skills,

    })


def youtube(request):
    intro = YouTubeIntro.objects.first()
    videos = YouTubeVideo.objects.all()
    return render(request, 'main/youtube.html', {
        'intro': intro,
        'videos': videos
    })
from django.shortcuts import get_object_or_404

def delete_video(request, pk):
    if request.method == 'POST':
        video = get_object_or_404(YouTubeVideo, pk=pk)
        video.delete()
    return redirect('dashboard')

from django.shortcuts import render, redirect
from .models import DashboardSecurity

def auth_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pin = request.POST.get('pin_code')
        creds = DashboardSecurity.objects.first()
        if creds and user == creds.username and pin == creds.pin_code:
            request.session['step1_passed'] = True
            return redirect('auth_nt')
        else:
            return render(request, 'main/auth_login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/auth_login.html')


def auth_nt(request):
    if not request.session.get('step1_passed'):
        return redirect('auth_login')
    
    if request.method == 'POST':
        nt = request.POST.get('nt_code')
        creds = DashboardSecurity.objects.first()
        if creds and nt == creds.nt_code:
            request.session['step2_passed'] = True
            return redirect('auth_bro')
        else:
            return render(request, 'main/auth_nt.html', {'error': 'Wrong NT code'})
    return render(request, 'main/auth_nt.html')


def auth_bro(request):
    if not request.session.get('step2_passed'):
        return redirect('auth_nt')
    
    if request.method == 'POST':
        bro = request.POST.get('bro_name')
        creds = DashboardSecurity.objects.first()
        if creds and bro == creds.best_bro_name:
            request.session['step3_passed'] = True
            return redirect('dashboard')
        else:
            return render(request, 'main/auth_bro.html', {'error': 'Wrong answer'})
    return render(request, 'main/auth_bro.html')

from django.shortcuts import redirect

def logout_auth(request):
    request.session.flush()  # clears all session data
    return redirect('auth_login')  # change this if your login URL name is different
