from django.shortcuts import render

from employees.models import Employee
from organizations.models import Organization


def dashboard_context():

    return {
        "organizations": Organization.objects.count(),
        "employees": Employee.objects.count(),
        # Курси/Тести/Сертифікати ще не реалізовані (Sprint 4-6)
        "courses": 0,
        "tests": 0,
        "certificates": 0,
    }


def home(request):
    return render(request, "dashboard.html", dashboard_context())


def courses(request):
    return render(request, "dashboard.html", dashboard_context())


def tests(request):
    return render(request, "dashboard.html", dashboard_context())


def certificates(request):
    return render(request, "dashboard.html", dashboard_context())


def reports(request):
    return render(request, "dashboard.html", dashboard_context())


def settings(request):
    return render(request, "dashboard.html", dashboard_context())
