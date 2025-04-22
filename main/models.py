from django.db import models
from django.utils import timezone
from datetime import timedelta

class PortoData(models.Model):

    summary = models.TextField(null=True, blank=True)  # 👈 Add this line
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed"

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='project_media/')
    is_video = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.file.name.lower().endswith(('.mp4', '.webm', '.mov')):
            self.is_video = True
        super().save(*args, **kwargs)

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField(default=False)
    is_starred = models.BooleanField(default=False)

    def time_left(self):
        if self.is_saved or self.is_starred:
            return None
        expire_time = self.timestamp + timedelta(days=30)
        return max(expire_time - timezone.now(), timedelta(seconds=0))

    def is_expired(self):
        return not (self.is_saved or self.is_starred) and self.timestamp < timezone.now() - timedelta(days=30)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class StarredMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField(default=False)
    is_starred = models.BooleanField(default=False)

    def time_left(self):
        if self.is_saved or self.is_starred:
            return None
        expire_time = self.timestamp + timedelta(days=30)
        return max(expire_time - timezone.now(), timedelta(seconds=0))

    def is_expired(self):
        return not (self.is_saved or self.is_starred) and self.timestamp < timezone.now() - timedelta(days=30)

    def __str__(self):
        return f"{self.name} ({self.email})"

class SavedMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_saved = models.BooleanField(default=False)
    is_starred = models.BooleanField(default=False)

    def time_left(self):
        if self.is_saved or self.is_starred:
            return None
        expire_time = self.timestamp + timedelta(days=30)
        return max(expire_time - timezone.now(), timedelta(seconds=0))

    def is_expired(self):
        return not (self.is_saved or self.is_starred) and self.timestamp < timezone.now() - timedelta(days=30)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_id = models.CharField(max_length=255, unique=True)
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
    
# class Experience(models.Model):
#     company = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     role = models.CharField(max_length=100)

# class Education(models.Model):
#     institution = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     field = models.CharField(max_length=100)

# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     level = models.CharField(max_length=50)

# class Certificate(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateField()
#     institution = models.CharField(max_length=100)

# class Language(models.Model):
#     name = models.CharField(max_length=100)
#     level = models.CharField(max_length=50)

# class Volunteering(models.Model):
#     organization = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     description = models.TextField()

class Summary(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  # First 50 chars for admin display

class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    issue_date = models.DateField()
    specialization = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name} at {self.institution}"

class Language(models.Model):
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.language} ({self.level})"

class Volunteering(models.Model):
    activity = models.CharField(max_length=150)
    dates = models.CharField(max_length=100)  # or DateField for start/end separately
    institution = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.activity} at {self.institution}"

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.skill} ({self.level})"
