from django.db import models

from courses.models import Course


class Lesson(models.Model):

    STATUS_CHOICES = [
        ("draft", "Чернетка"),
        ("published", "Опубліковано"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Назва уроку",
    )

    short_description = models.TextField(
        blank=True,
        verbose_name="Короткий опис",
    )

    content = models.TextField(
        blank=True,
        verbose_name="Текст уроку",
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="Порядок",
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name="Статус",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title