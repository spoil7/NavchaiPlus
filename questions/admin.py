from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "test",
        "order",
        "points",
        "is_active",
    )

    list_filter = (
        "test",
        "is_active",
    )

    search_fields = (
        "title",
        "test__title",
    )

    ordering = (
        "test",
        "order",
    )

    list_editable = (
        "order",
        "points",
        "is_active",
    )