from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm, TaskNotesForm
from tasks.models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "my_tasks": tasks,
    }
    return render(request, "tasks/show_my_tasks.html", context)


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        "task": task
    }
    return render(request, "tasks/task_detail.html", context)


@login_required
def add_notes(request, task_id):
    task = get_object_or_404(Task, id=task_id, assignee=request.user)
    if request.method == "POST":
        form = TaskNotesForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", task_id=task.id)
    else:
        form = TaskNotesForm(instance=task)
    context = {
        "form": form,
        "task": task,
    }
    return render(request, "tasks/add_notes.html", context)
