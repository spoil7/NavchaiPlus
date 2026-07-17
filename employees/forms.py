from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = [
            "organization",
            "full_name",
            "position",
            "email",
            "phone",
            "is_active",
        ]

        labels = {
            "organization": "Організація",
            "full_name": "ПІБ",
            "position": "Посада",
            "email": "Email",
            "phone": "Телефон",
            "is_active": "Активний",
        }

        widgets = {

            "organization": forms.Select(attrs={
                "class": "form-control",
            }),

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Прізвище Ім'я По батькові",
            }),

            "position": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Посада",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@organization.ua",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+380...",
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

        }
