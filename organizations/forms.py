from django import forms

from .models import Organization


class OrganizationForm(forms.ModelForm):

    class Meta:

        model = Organization

        fields = [
            "name",
            "edrpou",
            "city",
            "address",
            "email",
            "phone",
            "is_active",
        ]

        labels = {
            "name": "Назва",
            "edrpou": "ЄДРПОУ",
            "city": "Місто",
            "address": "Адреса",
            "email": "Email",
            "phone": "Телефон",
            "is_active": "Активна",
        }

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва організації",
            }),

            "edrpou": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Код ЄДРПОУ",
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Місто",
            }),

            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Адреса",
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