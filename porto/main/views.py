from django.shortcuts import render, redirect,get_object_or_404
from .forms import ExperienceForm ,ContactMessageForm, PortoForm, ProjectForm, ProjectMediaForm
from .models import ContactMessage, PortoData, Project, ProjectMedia
from .forms import ExperienceForm, EducationForm, SkillForm, CertificateForm, LanguageForm, VolunteeringForm
from .models import Summary
from .forms import SummaryForm

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
    project_form = ProjectForm()
    media_form = ProjectMediaForm()
    projects = Project.objects.all()
    from django.utils import timezone
    from datetime import timedelta
    messages = ContactMessage.objects.filter(is_saved=False, is_starred=False)
    starred = ContactMessage.objects.filter(is_starred=True)
    saved = ContactMessage.objects.filter(is_saved=True)
    ContactMessage.objects.filter(
        is_saved=False,
        is_starred=False,
        timestamp__lt=timezone.now() - timedelta(days=30)
    ).delete()
    

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
    summary, created = Summary.objects.get_or_create(pk=1)
    if request.method == 'POST' and 'summary' in request.POST:
        summary.content = request.POST.get('summary')
        summary.save()
        return redirect('dashboard')
    return render(request, 'main/dashboard.html', {
        'form': form,
        'project_form': project_form,
        'media_form': media_form,
        'projects': projects,
        'messages': messages,
        'starred': starred,
        'saved': saved,
        'summary': summary,
        'education_form': EducationForm(),
        'experience_form': ExperienceForm(),
        'skill_form': SkillForm(),
        'certificate_form': CertificateForm(),
        'language_form': LanguageForm(),
        'volunteering_form': VolunteeringForm(),
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


# from googleapiclient.discovery import build
# from django.conf import settings
# from .models import YouTubeVideo
# from datetime import datetime

# # Function to get YouTube API client
# def get_youtube_client():
#     return build('youtube', 'v3', developerKey=settings.AIzaSyA3Qk4xbc7B_RkpMWy2gygjkg4QsROEhfs)

# Function to fetch videos from your YouTube channel
# def fetch_youtube_videos():
#     # youtube = get_youtube_client()
#     request = youtube.search().list(
#         part="snippet",
#         channelId=settings.YOUTUBE_CHANNEL_ID,  # Replace with your actual channel ID
#         maxResults=50,  # Adjust this number as needed
#         order="date"
#     )
#     response = request.execute()
    
#     # Save videos to the database
#     for item in response.get("items", []):
#         video_id = item["id"]["videoId"]
#         title = item["snippet"]["title"]
#         description = item["snippet"]["description"]
#         published_at = datetime.strptime(item["snippet"]["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
#         thumbnail_url = item["snippet"]["thumbnails"]["high"]["url"]
        
#         # Check if the video is already saved in the database
#         video, created = YouTubeVideo.objects.get_or_create(
#             video_id=video_id,
#             defaults={'title': title, 'description': description, 'published_at': published_at, 'thumbnail_url': thumbnail_url}
#         )
#         if not created:
#             # Update existing video details
#             video.title = title
#             video.description = description
#             video.published_at = published_at
#             video.thumbnail_url = thumbnail_url
#             video.save()


# def youtube_view(request):
#     # Fetch YouTube videos from the database (or update them if needed)
#     fetch_youtube_videos()

#     # Get all videos to display on the page
#     videos = YouTubeVideo.objects.all().order_by('-published_at')

#     return render(request, 'youtube/youtube_page.html', {
#         'videos': videos
#     })

def cv(request):
    from .models import Experience, Education, Skill, Certificate, Language, Volunteering, PortoData
    summary = PortoData.objects.last().summary if PortoData.objects.last() else "No summary available."
    return render(request, 'main/cv.html', {
        'summary': summary,
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'skills': Skill.objects.all(),
        'certificates': Certificate.objects.all(),
        'languages': Language.objects.all(),
        'volunteering': Volunteering.objects.all(),
    })



def edit_summary(request):
    summary, _ = Summary.objects.get_or_create(pk=1)

    if request.method == 'POST':
        form = SummaryForm(request.POST, instance=summary)
        if form.is_valid():
            form.save()
            return redirect('edit_summary')  # redirect to itself
    else:
        form = SummaryForm(instance=summary)

    return render(request, 'dashboard/edit_summary.html', {'form': form})

def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')  # or 'dashboard' if that's the name

def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def add_language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

def add_volunteering(request):
    if request.method == 'POST':
        form = VolunteeringForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('dashboard')