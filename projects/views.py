from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from projects.forms import CreateProjectForm

# Create your views here.
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": project_list,
    }
    return render(request, "projects/list_projects.html", context)

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id, owner=request.user)
    tasks = Task.objects.filter(project=project)
    context = {
        "project": project,
        "tasks": tasks,
    }
    return render(request, "projects/project_details.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)
