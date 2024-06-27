from django.urls import path
from projects.views import list_projects, show_project, create_project, search_projects, company_list, add_company

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("search/", search_projects, name="search_projects"),
    path("companies/", company_list, name="company_list"),
    path("addcompany/", add_company, name="add_company"),
]
