from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project

# Create your views here.
def list_projects(request):
    project_list = Project.objects.filter(owner_id=request.user.id)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list_projects.html", context)
