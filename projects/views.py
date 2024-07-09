from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from projects.forms import CreateProjectForm, EditProjectForm


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

@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = EditProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('show_project', id=project.id)
    else:
        form = EditProjectForm(instance=project)
    context = {
        "form": form,
        "project": project,
    }
    return render(request, 'projects/edit_project.html', context)


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect("list_projects")
    context = {
        "project": project,
    }
    return render(request, "projects/delete_project.html", context)

@login_required
def delete_task_from_project_list(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("show_project", id=project_id)
    context = {
        "project": project,
        "task": task,
    }
    return render(request, "projects/delete_task.html", context)
