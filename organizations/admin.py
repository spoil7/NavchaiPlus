from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "city",
        "phone",
        "is_active"
    )

    search_fields = (
        "name",
        "city",
        "edrpou"
    )

    list_filter = (
        "city",
        "is_active"
    )