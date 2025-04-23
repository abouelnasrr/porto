from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactMessageForm, PortoForm, ProjectForm, ProjectMediaForm
from .models import ContactMessage, PortoData, Project, ProjectMedia
# from .forms import ExperienceForm, EducationForm, SkillForm, CertificateForm, LanguageForm, VolunteeringForm
from .models import Summary
from .forms import SummaryForm
from .models import Experience, Education
from .forms import ExperienceForm, EducationForm
from .models import Language, Volunteering, Skill
from .forms import LanguageForm, VolunteeringForm, SkillForm


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
    language_form = LanguageForm()
    languages = Language.objects.all()

    volunteering_form = VolunteeringForm()
    volunteerings = Volunteering.objects.all()

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
    
    ContactMessage.objects.filter(
        is_saved=False,
        is_starred=False,
        timestamp__lt=timezone.now() - timedelta(days=30)
    ).delete()
    
    if request.method == 'POST':
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
    # summary, created = Summary.objects.get_or_create(pk=1)
    # if request.method == 'POST' and 'summary' in request.POST:
        # summary.content = request.POST.get('summary')
        # summary.save()
        # return redirect('dashboard')
    return render(request, 'main/dashboard.html', {
        'form': form,
        'project_form': project_form,
        'media_form': media_form,
        'projects': projects,
        'messages': messages,
        'starred': starred,
        'saved': saved,
        # 'summary': summary,
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
    # from .models import Experience, Education, Skill, Certificate, Language, Volunteering, 
    from .models import PortoData
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    # experiences = Experience.objects.all()
    # educations = Education.objects.all()
    languages = Language.objects.all()
    volunteerings = Volunteering.objects.all()
    skills = Skill.objects.all()


    summary = PortoData.objects.last().summary if PortoData.objects.last() else "No summary available."
    return render(request, 'main/cv.html', {
        # 'summary': summary,
        'experiences': experiences,
        'educations': educations,
        'languages': languages,
        'volunteerings': volunteerings,
        'skills': skills,

    })



# def edit_summary(request):
#     summary, _ = Summary.objects.get_or_create(pk=1)

#     if request.method == 'POST':
#         form = SummaryForm(request.POST, instance=summary)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_summary')  # redirect to itself
#     else:
#         form = SummaryForm(instance=summary)

#     return render(request, 'dashboard/edit_summary.html', {'form': form})

