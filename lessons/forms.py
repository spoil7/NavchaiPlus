from django import forms

from .models import Lesson


class LessonForm(forms.ModelForm):

    class Meta:

        model = Lesson

        fields = [
            "course",
            "title",
            "short_description",
            "content",
            "order",
            "status",
        ]

        labels = {
            "course": "Курс",
            "title": "Назва уроку",
            "short_description": "Короткий опис",
            "content": "Зміст уроку",
            "order": "Порядок",
            "status": "Статус",
        }

        widgets = {

            "course": forms.Select(attrs={
                "class": "form-control",
            }),

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Назва уроку",
            }),

            "short_description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
            }),

            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 12,
            }),

            "order": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1,
            }),

            "status": forms.Select(attrs={
                "class": "form-control",
            }),

        }