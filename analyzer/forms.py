from django import forms 
from .models import Resume

class ResumeForm(forms.ModelForm):
    class  Meta:
        model = Resume
        fields = ['name', 'resume_file', 'job_description']
        widgets = {
            'job_description': forms.Textarea(attrs={'rows':5})
        }
