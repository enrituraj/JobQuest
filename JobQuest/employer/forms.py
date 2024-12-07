from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Job Description'}),
            'location': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Job Location'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter Job Salary'}),
        }
