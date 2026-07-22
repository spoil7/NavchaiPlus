from django.shortcuts import get_object_or_404, redirect, render

from .forms import QuestionForm
from .models import Question


def list_questions(request):
    questions = Question.objects.select_related("test").all()

    return render(
        request,
        "questions/list.html",
        {
            "questions": questions,
        },
    )


def detail_question(request, pk):
    question = get_object_or_404(
        Question.objects.select_related("test"),
        pk=pk,
    )

    return render(
        request,
        "questions/detail.html",
        {
            "question": question,
        },
    )


def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("questions:list")
    else:
        form = QuestionForm()

    return render(
        request,
        "questions/create.html",
        {
            "form": form,
        },
    )


def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            form.save()
            return redirect("questions:list")
    else:
        form = QuestionForm(instance=question)

    return render(
        request,
        "questions/edit.html",
        {
            "form": form,
            "question": question,
        },
    )


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        question.delete()
        return redirect("questions:list")

    return render(
        request,
        "questions/delete.html",
        {
            "question": question,
        },
    )