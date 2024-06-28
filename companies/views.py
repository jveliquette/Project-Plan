from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from companies.models import Company
from companies.forms import CompanyForm

# Create your views here.
@login_required
def company_list(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
    }
    return render(request, "companies/company_list.html", context)

@login_required
def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = CompanyForm()
    context = {
        "form": form,
    }
    return render(request, "companies/add_company.html", context)

@login_required
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = CompanyForm(instance=company)
    context = {
        "form": form,
        "company": company,
    }
    return render(request, "companies/edit_company.html", context)

@login_required
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        company.delete()
        return redirect("company_list")
    context = {
        "company": company,
    }
    return render(request, "companies/delete_company.html", context)
