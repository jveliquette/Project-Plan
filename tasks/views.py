from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm, TaskNotesForm, EditTaskForm
from tasks.models import Task, TaskChart
import pandas as pd
from plotly.offline import plot
import plotly.express as px

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
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
    project = task.project
    context = {
        "task": task,
        "project": project,
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

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, assignee=request.user)
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", task_id=task.id)
    else:
        form = EditTaskForm(instance=task)
    context = {
        "form": form,
        "task": task,
    }
    return render(request, "tasks/edit_task.html", context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")
    context = {
        "task": task,
    }
    return render(request, "tasks/delete_task.html", context)


def show_task_chart(request):
    tasks = Task.objects.filter(assignee=request.user)

    projects_data = [
        {
            "Project": f"{task.project.name} - {task.name}",
            "Start": task.start_date,
            "Finish": task.due_date,
            "Responsible": task.assignee.username if task.assignee else "Unassigned",
        }
        for task in tasks
    ]

    df = pd.DataFrame(projects_data)

    if not df.empty:
        fig = px.timeline(
            df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
        )
        fig.update_yaxes(autorange="reversed")

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Project - Task",
            plot_bgcolor='rgba(0,0,0,0)',  # transparent background
            paper_bgcolor='rgba(0,0,0,0)',  # transparent background
            font=dict(color="white"),
            legend=dict(
                title="Responsible",
                font=dict(
                    family="Roboto, sans-serif",
                    size=14,
                    color="white"
                )
            )
        )

        fig.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
        fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')

        gantt_plot = plot(fig, output_type="div")
    else:
        gantt_plot = "No data available to display the chart."

    context = {
        "tasks": tasks,
        "plot_div": gantt_plot,
    }

    return render(request, 'tasks/show_task_chart.html', context)
