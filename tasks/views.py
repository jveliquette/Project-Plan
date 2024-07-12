from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.forms import CreateTaskForm, TaskNotesForm, EditTaskForm
from tasks.models import Task
from projects.models import Project
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from plotly import graph_objs as go

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
    tasks = Task.objects.all()

    sort_by = request.GET.get('sort_by')

    if sort_by == 'project':
        tasks = tasks.order_by('project__name', 'name')
    elif sort_by == 'start_date':
        tasks = tasks.order_by('start_date')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif sort_by == 'completed':
        tasks = tasks.order_by('is_completed')

    projects_data = []
    for task in tasks:
        project_name = f"{task.project.name}"
        projects_data.append({
            "Task": task.name,
            "Project": project_name,
            "Start": task.start_date,
            "Finish": task.due_date,
            "Completed": task.is_completed,
        })

    df = pd.DataFrame(projects_data)
    if not df.empty:
        projects = Project.objects.all()
        color_map = px.colors.qualitative.Dark24[:len(projects)]
        project_color_map = {project.name: color_map[i % len(color_map)] for i, project in enumerate(projects)}
        df["Color"] = df.apply(lambda row: "#FFFFFF" if row["Completed"] else project_color_map.get(row["Project"], "#FFFFFF"), axis=1)

        fig = px.timeline(
            df, x_start="Start", x_end="Finish", y="Task", color="Project",
            labels={"Task": "Task", "Start": "Start Date", "Finish": "Due Date"},
            color_discrete_map=project_color_map,
            template="plotly_dark",
            opacity=0.95,
        )
        fig.update_yaxes(autorange="reversed")

        completed_tasks = df[df["Completed"]]
        fig.add_trace(go.Scatter(
            x=completed_tasks["Start"],
            y=completed_tasks["Task"],
            mode="markers",
            marker=dict(symbol="square", size=10, color="#FFFFFF", line=dict(width=3, color="Black")),
            showlegend=True,
            name="Completed Tasks",
            text="Completed",
            hoverinfo="text",
            opacity=0.8,
            hoverlabel=dict(
                bgcolor="white",
                font=dict(color="black")
            )
        ))

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Task",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color="white"),
            legend=dict(
                title="Project",
                font=dict(
                    family="Roboto, sans-serif",
                    size=14,
                    color="white"
                )
            )
        )

        fig.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
        fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')

        gantt_plot = fig.to_html(full_html=False, include_plotlyjs=False)
    else:
        gantt_plot = "No data available to display the chart."

    context = {
        "my_tasks": tasks,
        "plot_div": gantt_plot,
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
    task = get_object_or_404(Task, id=task_id)
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
    task = get_object_or_404(Task, id=task_id)
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


# @login_required
# def show_task_chart(request):
#     tasks = Task.objects.all()
#     projects_data = []
#     for task in tasks:
#         project_name = f"{task.project.name}"
#         projects_data.append({
#             "Task": task.name,
#             "Project": project_name,
#             "Start": task.start_date,
#             "Finish": task.due_date,
#             "Completed": task.is_completed,
#         })

#     df = pd.DataFrame(projects_data)
#     if not df.empty:
#         projects = Project.objects.all()
#         color_map = px.colors.qualitative.Dark24[:len(projects)]
#         project_color_map = {project.name: color_map[i % len(color_map)] for i, project in enumerate(projects)}
#         df["Color"] = df.apply(lambda row: "#FFFFFF" if row["Completed"] else project_color_map.get(row["Project"], "#FFFFFF"), axis=1)

#         fig = px.timeline(
#             df, x_start="Start", x_end="Finish", y="Task", color="Project",
#             labels={"Task": "Task", "Start": "Start Date", "Finish": "Due Date"},
#             color_discrete_map=project_color_map,
#             template="plotly_dark",
#             opacity=0.95,
#         )
#         fig.update_yaxes(autorange="reversed")

#         completed_tasks = df[df["Completed"]]
#         fig.add_trace(go.Scatter(
#             x=completed_tasks["Start"],
#             y=completed_tasks["Task"],
#             mode="markers",
#             marker=dict(symbol="square", size=10, color="#FFFFFF", line=dict(width=3, color="Black")),
#             showlegend=True,
#             name="Completed Tasks",
#             text="Completed",
#             hoverinfo="text",
#             opacity=0.8,
#             hoverlabel=dict(
#                 bgcolor="white",
#                 font=dict(color="black")
#             )
#         ))

#         fig.update_layout(
#             xaxis_title="Date",
#             yaxis_title="Task",
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             font=dict(color="white"),
#             legend=dict(
#                 title="Project",
#                 font=dict(
#                     family="Roboto, sans-serif",
#                     size=14,
#                     color="white"
#                 )
#             )
#         )

#         fig.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')
#         fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.2)')

#         gantt_plot = fig.to_html(full_html=False, include_plotlyjs=False)
#     else:
#         gantt_plot = "No data available to display the chart."

#     context = {
#         "tasks": tasks,
#         "plot_div": gantt_plot,
#     }

#     return render(request, 'tasks/show_task_chart.html', context)
