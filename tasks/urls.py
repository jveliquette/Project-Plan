from django.urls import path
from tasks.views import create_task, show_my_tasks, task_detail, add_notes

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:task_id>/", task_detail, name="task_detail"),
    path("<int:task_id>/addnotes/", add_notes, name="add_notes")
]
