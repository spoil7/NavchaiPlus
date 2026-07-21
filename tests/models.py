from django.db import models

from courses.models import Course


class Test(models.Model):

    STATUS_CHOICES = [
        ("draft", "Чернетка"),
        ("published", "Опубліковано"),
    ]

    title = models.CharField(
        max_length=255,
        verbose_name="Назва",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Опис",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="tests",
        verbose_name="Курс",
    )

    passing_score = models.PositiveIntegerField(
        default=80,
        verbose_name="Прохідний бал (%)",
    )

    time_limit = models.PositiveIntegerField(
        default=30,
        verbose_name="Час (хв)",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Тест"
        verbose_name_plural = "Тести"

    def __str__(self):
        return self.title