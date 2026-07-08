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

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва організації"
            }),

            "edrpou": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "city": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "address": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }
