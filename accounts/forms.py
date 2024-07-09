from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LogInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "input"}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"class": "input"}))


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class": "input"}))
    password = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"class": "input"}))
    password_confirmation = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={"class": "input"}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken!")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("Passwords do not match!")

        return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Unrecognized username and/or password!",
    }
