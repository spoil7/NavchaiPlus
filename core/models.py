from django.db import models


class Organization(models.Model):
    name = models.CharField("Назва", max_length=255)
    code = models.CharField("Код ЄДРПОУ", max_length=20, blank=True)
    city = models.CharField("Місто", max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Організація"
        verbose_name_plural = "Організації"

    def __str__(self):
        return self.name


class Department(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    name = models.CharField("Назва", max_length=150)

    class Meta:
        verbose_name = "Підрозділ"
        verbose_name_plural = "Підрозділи"

    def __str__(self):
        return self.name


class Employee(models.Model):

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    full_name = models.CharField("ПІБ", max_length=255)

    position = models.CharField("Посада", max_length=150)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"

    def __str__(self):
        return self.full_name


class Course(models.Model):

    title = models.CharField("Назва", max_length=255)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"

    def __str__(self):
        return self.title


class Test(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)

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