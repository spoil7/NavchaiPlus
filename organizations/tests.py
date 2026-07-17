from django.test import TestCase

from .forms import OrganizationForm
from .models import Organization


class OrganizationEdrpouTests(TestCase):

    def test_edrpou_valid_8_digits_is_accepted(self):

        form = OrganizationForm(data={
            "name": "Лікарня №1",
            "edrpou": "12345678",
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_edrpou_valid_10_digits_fop_is_accepted(self):

        form = OrganizationForm(data={
            "name": "ФОП Іваненко",
            "edrpou": "1234567890",
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_edrpou_wrong_length_is_rejected(self):

        form = OrganizationForm(data={
            "name": "Лікарня №2",
            "edrpou": "123",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("edrpou", form.errors)

    def test_edrpou_blank_is_allowed(self):

        form = OrganizationForm(data={
            "name": "Без коду",
            "edrpou": "",
        })

        self.assertTrue(form.is_valid(), form.errors)

    def test_edrpou_duplicate_is_rejected(self):

        Organization.objects.create(
            name="Перша організація",
            edrpou="12345678",
        )

        form = OrganizationForm(data={
            "name": "Друга організація",
            "edrpou": "12345678",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("edrpou", form.errors)

    def test_edrpou_unique_check_ignores_current_instance_on_edit(self):

        organization = Organization.objects.create(
            name="Організація",
            edrpou="12345678",
        )

        form = OrganizationForm(
            data={
                "name": "Організація (оновлена назва)",
                "edrpou": "12345678",
            },
            instance=organization,
        )

        self.assertTrue(form.is_valid(), form.errors)
