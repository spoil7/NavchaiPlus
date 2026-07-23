from django.urls import path

from . import views

app_name = "answers"

urlpatterns = [
    path("", views.AnswerListView.as_view(), name="list"),
    path("<int:pk>/", views.AnswerDetailView.as_view(), name="detail"),
    path("create/", views.AnswerCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.AnswerUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.AnswerDeleteView.as_view(), name="delete"),
]