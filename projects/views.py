from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project, Company
from tasks.models import Task
from projects.forms import CreateProjectForm, ProjectSearchForm


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


def search_projects(request):
    form = ProjectSearchForm()
    projects = None
    if "company" in request.GET:
        form = ProjectSearchForm(request.GET)
        if form.is_valid():
            company = form.cleaned_data['company']
            projects = Project.objects.filter(company=company)
    context = {
        "form": form,
        "projects": projects,
    }
    return render(request, "projects/search_projects.html", context)
