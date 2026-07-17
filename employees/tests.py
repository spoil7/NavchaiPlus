from django.test import TestCase
from django.urls import reverse

from organizations.models import Organization
from .models import Employee


class EmployeeCrudTests(TestCase):

    def setUp(self):

        self.organization = Organization.objects.create(
            name="Лікарня №1",
            city="Київ",
        )

    def test_list_view_shows_only_matching_organization(self):

        other_org = Organization.objects.create(name="Лікарня №2")

        Employee.objects.create(
            organization=self.organization,
            full_name="Іваненко Іван",
        )

        Employee.objects.create(
            organization=other_org,
            full_name="Петренко Петро",
        )

        response = self.client.get(
            reverse("employees:list"),
            {"organization": self.organization.pk},
        )

        self.assertContains(response, "Іваненко Іван")
        self.assertNotContains(response, "Петренко Петро")

    def test_create_employee(self):

        response = self.client.post(
            reverse("employees:create"),
            {
                "organization": self.organization.pk,
                "full_name": "Коваленко Марія",
                "position": "Лаборант",
                "email": "",
                "phone": "",
            },
        )

        self.assertEqual(Employee.objects.count(), 1)

        employee = Employee.objects.first()

        self.assertRedirects(
            response,
            reverse("employees:detail", args=[employee.pk]),
        )

    def test_edit_employee(self):

        employee = Employee.objects.create(
            organization=self.organization,
            full_name="Стара Назва",
        )

        self.client.post(
            reverse("employees:edit", args=[employee.pk]),
            {
                "organization": self.organization.pk,
                "full_name": "Нова Назва",
                "position": "",
                "email": "",
                "phone": "",
                "is_active": "on",
            },
        )

        employee.refresh_from_db()

        self.assertEqual(employee.full_name, "Нова Назва")

    def test_delete_employee_requires_post(self):

        employee = Employee.objects.create(
            organization=self.organization,
            full_name="До видалення",
        )

        # GET should only show the confirmation page, not delete
        self.client.get(reverse("employees:delete", args=[employee.pk]))
        self.assertEqual(Employee.objects.count(), 1)

        self.client.post(reverse("employees:delete", args=[employee.pk]))
        self.assertEqual(Employee.objects.count(), 0)

    def test_organization_employees_related_name(self):

        Employee.objects.create(
            organization=self.organization,
            full_name="Тест Тестович",
        )

        self.assertEqual(self.organization.employees.count(), 1)
