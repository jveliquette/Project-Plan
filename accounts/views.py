from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import LogInForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LogInForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")
