from django.urls import path
from projects.views import list_projects, show_project, create_project, search_projects, delete_project, delete_task_from_project_list, edit_project

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("<int:id>/edit/", edit_project, name="edit_project"),
    path("create/", create_project, name="create_project"),
    path("search/", search_projects, name="search_projects"),
    path("<int:project_id>/delete/", delete_project, name="delete_project"),
    path("<int:project_id>/<int:task_id>/delete/", delete_task_from_project_list, name="delete_task_from_project_list")
]
