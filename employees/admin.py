from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "organization",
        "position",
        "is_active",
    )

    search_fields = (
        "full_name",
        "position",
        "organization__name",
    )

    list_filter = (
        "organization",
        "is_active",
    )
