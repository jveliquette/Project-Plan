from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from projects.models import Project
from companies.models import Company

class CreateProjectForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
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
            "owner": forms.HiddenInput(),
            "company": forms.Select(attrs={"class": "select"}),
        }

class ProjectSearchForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True, widget=forms.Select(attrs={"class": "select"}))

class EditProjectForm(ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "company",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input", "placeholder": "Enter project name..."}),
            "description": forms.Textarea(attrs={"class": "textarea", "placeholder": "Enter project description..."}),
            "company": forms.Select(attrs={"class": "select"}),
        }
