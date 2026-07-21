from django import forms

from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = [
            "title",
            "short_description",
            "duration",
            "status",
        ]

        labels = {
            "title": "Назва курсу",
            "short_description": "Короткий опис",
            "duration": "Тривалість (хв)",
            "status": "Статус",
        }

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Наприклад: Основи кібергігієни",
            }),

            "short_description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Короткий опис курсу",
            }),

            "duration": forms.NumberInput(attrs={
                "class": "form-control",
            }),

            "status": forms.Select(attrs={
                "class": "form-control",
            }),

        }