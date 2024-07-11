from django.urls import path, include
from tasks.views import create_task, show_my_tasks, task_detail, add_notes, edit_task, delete_task

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:task_id>/", task_detail, name="task_detail"),
    path("<int:task_id>/add-notes/", add_notes, name="add_notes"),
    path("<int:task_id>/edit-task/", edit_task, name="edit_task"),
    path("<int:task_id>/delete/", delete_task, name="delete_task"),
]
