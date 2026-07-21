from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Course
from .forms import CourseForm
from lessons.models import Lesson


def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            course = form.save()

            return redirect(
                "courses:detail",
                pk=course.pk,
            )

    else:

        form = CourseForm()

    return render(
        request,
        "courses/create.html",
        {
            "form": form,
        },
    )


def course_list(request):

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "all")
    sort = request.GET.get("sort", "name_asc")

    courses = Course.objects.all()

    if query:
        courses = courses.filter(
            Q(title__icontains=query)
            | Q(short_description__icontains=query)
        )

    if status != "all":
        courses = courses.filter(status=status)

    sort_options = {
        "name_asc": "title",
        "name_desc": "-title",
        "newest": "-id",
        "oldest": "id",
    }

    courses = courses.order_by(
        sort_options.get(sort, "title")
    )

    context = {
        "courses": courses,
        "query": query,
        "status": status,
        "sort": sort,
        "total_courses": Course.objects.count(),
        "active_courses": Course.objects.filter(status="active").count(),
        "inactive_courses": Course.objects.filter(status="inactive").count(),
    }

    return render(
        request,
        "courses/list.html",
        context,
    )


def course_detail(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk,
    )

    lessons = (
        Lesson.objects
        .filter(course=course)
        .order_by("order", "title")
    )

    context = {
        "course": course,
        "lessons": lessons,
        "lesson_count": lessons.count(),
        "published_lessons": lessons.filter(
            status="published"
        ).count(),
    }

    return render(
        request,
        "courses/detail.html",
        context,
    )


def course_edit(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk,
    )

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "courses:detail",
                pk=course.pk,
            )

    else:

        form = CourseForm(
            instance=course,
        )

    return render(
        request,
        "courses/edit.html",
        {
            "course": course,
            "form": form,
        },
    )


def course_delete(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk,
    )

    if request.method == "POST":

        course.delete()

        return redirect(
            "courses:list",
        )

    return render(
        request,
        "courses/delete.html",
        {
            "course": course,
        },
    )