from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TestForm
from .models import Test


def test_list(request):

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "all")
    sort = request.GET.get("sort", "name_asc")

    tests = Test.objects.select_related("course")

    if query:
        tests = tests.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(course__title__icontains=query)
        )

    if status != "all":
        tests = tests.filter(status=status)

    sort_options = {
        "name_asc": "title",
        "name_desc": "-title",
        "newest": "-created_at",
        "oldest": "created_at",
    }

    tests = tests.order_by(
        sort_options.get(sort, "title")
    )

    context = {
        "tests": tests,
        "query": query,
        "status": status,
        "sort": sort,
        "total_tests": Test.objects.count(),
        "published_tests": Test.objects.filter(
            status="published"
        ).count(),
        "draft_tests": Test.objects.filter(
            status="draft"
        ).count(),
    }

    return render(
        request,
        "tests/list.html",
        context,
    )


def test_detail(request, pk):

    test = get_object_or_404(
        Test.objects.select_related("course"),
        pk=pk,
    )

    return render(
        request,
        "tests/detail.html",
        {
            "test": test,
        },
    )


def test_create(request):

    if request.method == "POST":

        form = TestForm(request.POST)

        if form.is_valid():

            test = form.save()

            return redirect(
                "tests:detail",
                pk=test.pk,
            )

    else:

        form = TestForm()

    return render(
        request,
        "tests/create.html",
        {
            "form": form,
        },
    )


def test_edit(request, pk):

    test = get_object_or_404(
        Test,
        pk=pk,
    )

    if request.method == "POST":

        form = TestForm(
            request.POST,
            instance=test,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "tests:detail",
                pk=test.pk,
            )

    else:

        form = TestForm(
            instance=test,
        )

    return render(
        request,
        "tests/edit.html",
        {
            "form": form,
            "test": test,
        },
    )


def test_delete(request, pk):

    test = get_object_or_404(
        Test,
        pk=pk,
    )

    if request.method == "POST":

        test.delete()

        return redirect(
            "tests:list",
        )

    return render(
        request,
        "tests/delete.html",
        {
            "test": test,
        },
    )