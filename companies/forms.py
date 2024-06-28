from django.forms import ModelForm
from companies.models import Company
from django import forms

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "name",
            "address",
            "website",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "input", "placeholder": "Enter company name..."}),
            "address": forms.TextInput(attrs={"class": "input", "placeholder": "Enter company's physical address..."}),
            "website": forms.TextInput(attrs={"class": "input", "placeholder": "Enter company's website..."}),
        }
