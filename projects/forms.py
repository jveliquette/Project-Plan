from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from projects.models import Project

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input", "placeholder": "Enter project name..."}),
            "description": forms.Textarea(attrs={"class": "textarea", "placeholder": "Enter project description..."}),
            "owner": forms.HiddenInput(),
        }



class EditProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input", "placeholder": "Enter project name..."}),
            "description": forms.Textarea(attrs={"class": "textarea", "placeholder": "Enter project description..."}),
        }
