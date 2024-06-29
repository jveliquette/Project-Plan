from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
        )
    widgets = {
        "username": forms.TextInput(attrs={"class": "input"}),
        "password": forms.PasswordInput(attrs={"class": "input"}),
    }


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
        )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
        )
    widgets = {
        "username": forms.TextInput(attrs={"class": "input"}),
        "password": forms.PasswordInput(attrs={"class": "input"}),
        "password_confirmation": forms.PasswordInput(attrs={"class": "input"})
    }
