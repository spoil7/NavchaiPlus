from django.urls import path

from . import views

app_name = "tests"

urlpatterns = [

    path(
        "",
        views.test_list,
        name="list",
    ),

    path(
        "create/",
        views.test_create,
        name="create",
    ),

    path(
        "<int:pk>/",
        views.test_detail,
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        views.test_edit,
        name="edit",
    ),

    path(
        "<int:pk>/delete/",
        views.test_delete,
        name="delete",
    ),

]