from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.courses, name="courses"),
    path("tests/", views.tests, name="tests"),
    path("certificates/", views.certificates, name="certificates"),
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
]
