from django.contrib import admin

from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "passing_score",
        "time_limit",
        "status",
    )

    list_filter = (
        "status",
        "course",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "title",
    )