from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "test",
            "title",
            "order",
            "points",
            "is_active",
        ]

        labels = {
            "test": "Тест",
            "title": "Питання",
            "order": "Порядок",
            "points": "Кількість балів",
            "is_active": "Активне",
        }

        widgets = {
            "test": forms.Select(attrs={
                "class": "form-control"
            }),
            "title": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Введіть текст питання..."
            }),
            "order": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "points": forms.NumberInput(attrs={
                "class": "form-control"
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }