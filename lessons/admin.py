from django.contrib import admin

from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "order",
        "status",
    )

    list_filter = (
        "course",
        "status",
    )

    search_fields = (
        "title",
        "short_description",
    )