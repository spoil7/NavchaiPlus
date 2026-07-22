from django.urls import path

from . import views

app_name = "questions"

urlpatterns = [
    path("", views.list_questions, name="list"),
    path("<int:pk>/", views.detail_question, name="detail"),
    path("create/", views.create_question, name="create"),
    path("<int:pk>/edit/", views.edit_question, name="edit"),
    path("<int:pk>/delete/", views.delete_question, name="delete"),
]