from django import forms
from .models import PortoData, ContactMessage, Project, ProjectMedia
from .models import Experience, Education, Skill, Certificate, Language, Volunteering
from .models import Summary


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


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full p-4 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring focus:border-blue-300',
                'rows': 6,
                'placeholder': 'Write a short professional summary...'
            }),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class VolunteeringForm(forms.ModelForm):
    class Meta:
        model = Volunteering
        fields = '__all__'