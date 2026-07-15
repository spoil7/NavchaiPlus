from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Organization
from .forms import OrganizationForm


def organization_create(request):

    if request.method == "POST":
        form = OrganizationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("organizations:list")

    else:
        form = OrganizationForm()

    return render(
        request,
        "organizations/create.html",
        {
            "form": form,
        },
    )


def organization_list(request):

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "all")

    organizations = Organization.objects.all()

    if query:
        organizations = organizations.filter(
            Q(name__icontains=query)
            | Q(city__icontains=query)
            | Q(edrpou__icontains=query)
        )

    if status == "active":
        organizations = organizations.filter(is_active=True)

    elif status == "inactive":
        organizations = organizations.filter(is_active=False)

    organizations = organizations.order_by("name")

    context = {
        "organizations": organizations,
        "query": query,
        "status": status,
    }

    return render(
        request,
        "organizations/list.html",
        context,
    )


def organization_detail(request, pk):

    organization = get_object_or_404(
        Organization,
        pk=pk,
    )

    context = {
        "organization": organization,
    }

    return render(
        request,
        "organizations/detail.html",
        context,
    )