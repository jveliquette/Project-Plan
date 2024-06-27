from django.urls import path
from companies.views import company_list, add_company, edit_company

urlpatterns = [
    path("", company_list, name="company_list"),
    path("add/", add_company, name="add_company"),
    path("<int:company_id>/edit/", edit_company, name="edit_company")
]
