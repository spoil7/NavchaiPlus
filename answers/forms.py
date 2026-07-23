from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "question",
            "text",
            "is_correct",
            "order",
        ]

        widgets = {
            "question": forms.Select(attrs={"class": "form-select"}),
            "text": forms.TextInput(attrs={"class": "form-control"}),
            "is_correct": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "order": forms.NumberInput(attrs={"class": "form-control"}),
        }