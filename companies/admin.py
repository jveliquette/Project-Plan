from django.contrib import admin
from companies.models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
        "website",
    ]
