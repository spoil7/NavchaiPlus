from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    full_name = models.CharField("ПІБ", max_length=255)
    position = models.CharField("Посада", max_length=150)
    department = models.CharField("Відділення", max_length=150)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)

    is_active = models.BooleanField("Активний", default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField("Назва", max_length=255)
    description = models.TextField("Опис", blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField("Назва", max_length=255)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="tests"
    )

    pass_score = models.IntegerField(default=80)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тести"

    def __str__(self):
        return self.title


class Certificate(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    issued_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Сертифікат"
        verbose_name_plural = "Сертифікати"

    def __str__(self):
        return f"{self.employee} - {self.course}"