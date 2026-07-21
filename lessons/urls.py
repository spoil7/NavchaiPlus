from django.urls import path

from . import views

app_name = "lessons"

urlpatterns = [

    path(
        "",
        views.lesson_list,
        name="list",
    ),

    path(
        "create/",
        views.lesson_create,
        name="create",
    ),

    path(
        "<int:pk>/",
        views.lesson_detail,
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        views.lesson_edit,
        name="edit",
    ),

    path(
        "<int:pk>/delete/",
        views.lesson_delete,
        name="delete",
    ),

]