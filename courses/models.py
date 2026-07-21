from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    STATUS_CHOICES = [
        ("draft", "Чернетка"),
        ("published", "Опубліковано"),
        ("archived", "Архів"),
    ]

    title = models.CharField("Назва", max_length=200)
    short_description = models.TextField("Короткий опис", blank=True)

    duration = models.PositiveIntegerField(
        "Тривалість (хвилин)",
        default=0
    )

    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ["title"]

    def __str__(self):
        return self.title