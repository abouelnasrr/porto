from django import forms
from .models import Experience, PortoData, ContactMessage, Project, ProjectMedia
# from .models import Experience, Education, Skill, Certificate, Language, Volunteering
from .models import  Education


class PortoForm(forms.ModelForm):
    class Meta:
        model = PortoData
        fields = ['name', 'title', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'title': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'photo': forms.FileInput(attrs={'class': 'text-white'}),
        }
    

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'whatsapp', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Your email'}),
            'whatsapp': forms.TextInput(attrs={'class': 'input', 'placeholder': 'WhatsApp Number'}),
            'message': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Your message...'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'duration': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }

class ProjectMediaForm(forms.ModelForm):
    class Meta:
        model = ProjectMedia
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'text-white'}),  # Just use ClearableFileInput without 'multiple'
        }


# class SummaryForm(forms.ModelForm):
#     class Meta:
#         model = Summary
#         fields = ['content']
#         widgets = {
#             'content': forms.Textarea(attrs={
#                 'class': 'w-full p-4 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring focus:border-blue-300',
#                 'rows': 6,
#                 'placeholder': 'Write a short professional summary...'
#             }),
#         }

# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = '__all__'

# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = '__all__'

# class SkillForm(forms.ModelForm):
#     class Meta:
#         model = Skill
#         fields = '__all__'

# class CertificateForm(forms.ModelForm):
#     class Meta:
#         model = Certificate
#         fields = '__all__'

# class LanguageForm(forms.ModelForm):
#     class Meta:
#         model = Language
#         fields = '__all__'

# class VolunteeringForm(forms.ModelForm):
#     class Meta:
#         model = Volunteering
#         fields = '__all__'



class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'company': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'institution', 'issue_date', 'specialization']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'institution': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'specialization': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }


from .models import Language, Volunteering, Skill

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'level']
        widgets = {
            'language': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'level': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }

class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = ['activity', 'dates', 'institution']
        widgets = {
            'activity': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'dates': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'institution': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill', 'level']
        widgets = {
            'skill': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'level': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }


from .models import YouTubeIntro, YouTubeVideo

class YouTubeIntroForm(forms.ModelForm):
    class Meta:
        model = YouTubeIntro
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white', 'rows': 4})
        }

class YouTubeVideoForm(forms.ModelForm):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
            'url': forms.URLInput(attrs={'class': 'w-full p-2 rounded bg-gray-700 text-white'}),
        }
