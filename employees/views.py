from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from organizations.models import Organization
from .models import Employee
from .forms import EmployeeForm


def employee_create(request):

    organization_id = request.GET.get("organization")

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():

            employee = form.save()

            return redirect(
                "employees:detail",
                pk=employee.pk,
            )

    else:

        initial = {}

        if organization_id:
            initial["organization"] = organization_id

        form = EmployeeForm(initial=initial)

    return render(
        request,
        "employees/create.html",
        {
            "form": form,
        },
    )


def employee_list(request):

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "all")
    sort = request.GET.get("sort", "name_asc")
    organization_id = request.GET.get("organization", "")

    employees = Employee.objects.select_related("organization").all()

    if query:

        employees = employees.filter(
            Q(full_name__icontains=query)
            | Q(position__icontains=query)
            | Q(organization__name__icontains=query)
        )

    if organization_id:

        employees = employees.filter(
            organization_id=organization_id,
        )

    if status == "active":

        employees = employees.filter(
            is_active=True,
        )

    elif status == "inactive":

        employees = employees.filter(
            is_active=False,
        )

    sort_options = {
        "name_asc": "full_name",
        "name_desc": "-full_name",
        "newest": "-id",
        "oldest": "id",
    }

    employees = employees.order_by(
        sort_options.get(sort, "full_name")
    )

    selected_organization = None

    if organization_id:

        selected_organization = Organization.objects.filter(
            pk=organization_id,
        ).first()

    context = {
        "employees": employees,
        "query": query,
        "status": status,
        "sort": sort,
        "organization_id": organization_id,
        "selected_organization": selected_organization,
    }

    return render(
        request,
        "employees/list.html",
        context,
    )


def employee_detail(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk,
    )

    context = {
        "employee": employee,
    }

    return render(
        request,
        "employees/detail.html",
        context,
    )


def employee_edit(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk,
    )

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            instance=employee,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "employees:detail",
                pk=employee.pk,
            )

    else:

        form = EmployeeForm(
            instance=employee,
        )

    context = {
        "employee": employee,
        "form": form,
    }

    return render(
        request,
        "employees/edit.html",
        context,
    )


def employee_delete(request, pk):

    employee = get_object_or_404(
        Employee,
        pk=pk,
    )

    if request.method == "POST":

        employee.delete()

        return redirect(
            "employees:list",
        )

    context = {
        "employee": employee,
    }

    return render(
        request,
        "employees/delete.html",
        context,
    )
