from django.forms import ModelForm
from django import forms
from projects.models import Project, Company

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
            "company",
        ]

class ProjectSearchForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=True)

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "address",
            "website",
        ]
