from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course
from .forms import LessonForm
from .models import Lesson


def lesson_list(request):

    query = request.GET.get("q", "").strip()
    course_id = request.GET.get("course")
    status = request.GET.get("status", "all")
    sort = request.GET.get("sort", "title")

    lessons = Lesson.objects.select_related("course").all()

    if course_id:
        lessons = lessons.filter(course_id=course_id)

    if query:
        lessons = lessons.filter(
            Q(title__icontains=query)
            | Q(short_description__icontains=query)
            | Q(course__title__icontains=query)
        )

    if status != "all":
        lessons = lessons.filter(status=status)

    sort_options = {
        "title": "title",
        "-title": "-title",
        "order": "order",
        "-order": "-order",
        "newest": "-created_at",
        "oldest": "created_at",
    }

    lessons = lessons.order_by(
        sort_options.get(sort, "order")
    )

    context = {
        "lessons": lessons,
        "query": query,
        "status": status,
        "sort": sort,
        "selected_course": course_id,
        "courses": Course.objects.all().order_by("title"),

        "total_lessons": Lesson.objects.count(),
        "published_lessons": Lesson.objects.filter(
            status="published"
        ).count(),
        "draft_lessons": Lesson.objects.filter(
            status="draft"
        ).count(),
    }

    return render(
        request,
        "lessons/list.html",
        context,
    )


def lesson_create(request):

    initial = {}

    course_id = request.GET.get("course")

    if course_id:
        initial["course"] = course_id

    if request.method == "POST":

        form = LessonForm(
            request.POST,
            initial=initial,
        )

        if form.is_valid():

            lesson = form.save()

            messages.success(
                request,
                "Урок успішно створено."
            )

            if lesson.course_id:
                return redirect(
                    f"/courses/{lesson.course_id}/"
                )

            return redirect(
                "lessons:list"
            )

    else:

        form = LessonForm(
            initial=initial
        )

    return render(
        request,
        "lessons/create.html",
        {
            "form": form,
        },
    )


def lesson_detail(request, pk):

    lesson = get_object_or_404(
        Lesson.objects.select_related("course"),
        pk=pk,
    )

    return render(
        request,
        "lessons/detail.html",
        {
            "lesson": lesson,
        },
    )


def lesson_edit(request, pk):

    lesson = get_object_or_404(
        Lesson,
        pk=pk,
    )

    if request.method == "POST":

        form = LessonForm(
            request.POST,
            instance=lesson,
        )

        if form.is_valid():

            lesson = form.save()

            messages.success(
                request,
                "Урок успішно оновлено."
            )

            return redirect(
                "lessons:detail",
                pk=lesson.pk,
            )

    else:

        form = LessonForm(
            instance=lesson,
        )

    return render(
        request,
        "lessons/edit.html",
        {
            "lesson": lesson,
            "form": form,
        },
    )


def lesson_delete(request, pk):

    lesson = get_object_or_404(
        Lesson,
        pk=pk,
    )

    course_id = lesson.course_id

    if request.method == "POST":

        lesson.delete()

        messages.success(
            request,
            "Урок видалено."
        )

        if course_id:
            return redirect(
                f"/courses/{course_id}/"
            )

        return redirect(
            "lessons:list"
        )

    return render(
        request,
        "lessons/delete.html",
        {
            "lesson": lesson,
        },
    )