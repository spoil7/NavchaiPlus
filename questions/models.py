from django.db import models
from tests.models import Test


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Тест"
    )

    title = models.TextField(
        verbose_name="Питання"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="Порядок"
    )

    points = models.PositiveIntegerField(
        default=1,
        verbose_name="Бали"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Активне"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Питання"
        verbose_name_plural = "Питання"
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title[:70]}"