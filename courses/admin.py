from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "duration",
        "status",
        "created_at",
    )

    list_filter = ("status",)
    search_fields = ("title",)