from django.db import models


class Organization(models.Model):
    name = models.CharField(
        "Назва",
        max_length=255
    )

    edrpou = models.CharField(
        "ЄДРПОУ",
        max_length=20,
        blank=True
    )

    city = models.CharField(
        "Місто",
        max_length=120,
        blank=True
    )

    address = models.CharField(
        "Адреса",
        max_length=255,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Організація"
        verbose_name_plural = "Організації"

    def __str__(self):
        return self.name