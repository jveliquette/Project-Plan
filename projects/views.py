from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project

# Create your views here.
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list_projects.html", context)
