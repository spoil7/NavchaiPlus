from django.shortcuts import render
from .models import Organization
from django.shortcuts import redirect
from .forms import OrganizationForm
from django.shortcuts import get_object_or_404
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
            "form": form
        }
    )
def organization_list(request):

    organizations = Organization.objects.all().order_by("name")

    context = {
        "organizations": organizations,
    }

    return render(
        request,
        "organizations/list.html",
        context,
    )
def organization_detail(request, pk):

    organization = get_object_or_404(
        Organization,
        pk=pk
    )

    context = {
        "organization": organization
    }

    return render(
        request,
        "organizations/detail.html",
        context
    )