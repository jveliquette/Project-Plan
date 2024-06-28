from django.forms import ModelForm
from django import forms
from projects.models import Project
from companies.models import Company

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
            "company",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input", "placeholder": "Enter project name..."}),
            "description": forms.Textarea(attrs={"class": "textarea", "placeholder": "Enter project description..."}),
            "owner": forms.Select(attrs={"class": "select"}),
            "company": forms.Select(attrs={"class": "select"}),
        }

class ProjectSearchForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True, widget=forms.Select(attrs={"class": "select"}))
