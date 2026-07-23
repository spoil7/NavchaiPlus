from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Answer
from .forms import AnswerForm


class AnswerListView(ListView):
    model = Answer
    template_name = "answers/list.html"
    context_object_name = "answers"


class AnswerDetailView(DetailView):
    model = Answer
    template_name = "answers/detail.html"
    context_object_name = "answer"


class AnswerCreateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answers/create.html"
    success_url = reverse_lazy("answers:list")


class AnswerUpdateView(UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answers/edit.html"
    success_url = reverse_lazy("answers:list")


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = "answers/delete.html"
    success_url = reverse_lazy("answers:list")