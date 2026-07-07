from django.shortcuts import render
from .models import Course, Employee, Test, Certificate

def dashboard_context():
    return {
        "courses": Course.objects.count(),
        "employees": Employee.objects.count(),
        "tests": Test.objects.count(),
        "certificates": Certificate.objects.count(),
    }


def home(request):
    context = {
        "courses": Course.objects.count(),
        "employees": Employee.objects.count(),
        "tests": Test.objects.count(),
        "certificates": Certificate.objects.count(),
    }

    return render(request, "dashboard.html", context)


def home(request):
    return render(request, "dashboard.html", dashboard_context())


def courses(request):
    return render(request, "dashboard.html", dashboard_context())


def tests(request):
    return render(request, "dashboard.html", dashboard_context())


def employees(request):
    return render(request, "dashboard.html", dashboard_context())


def certificates(request):
    return render(request, "dashboard.html", dashboard_context())


def reports(request):
    return render(request, "dashboard.html", dashboard_context())


def settings(request):
    return render(request, "dashboard.html", dashboard_context())
from .models import Course, Employee, Test, Certificate 
