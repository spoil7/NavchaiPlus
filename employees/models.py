from django.db import models

from organizations.models import Organization


class Employee(models.Model):

    organization = models.ForeignKey(
        Organization,
        verbose_name="Організація",
        on_delete=models.CASCADE,
        related_name="employees",
    )

    full_name = models.CharField(
        "ПІБ",
        max_length=255,
    )

    position = models.CharField(
        "Посада",
        max_length=150,
        blank=True,
    )

    email = models.EmailField(
        "Email",
        blank=True,
    )

    phone = models.CharField(
        "Телефон",
        max_length=30,
        blank=True,
    )

    is_active = models.BooleanField(
        "Активний",
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
