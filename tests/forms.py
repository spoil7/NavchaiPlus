from django import forms

from .models import Test


class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = [
            "title",
            "description",
            "course",
            "passing_score",
            "time_limit",
            "status",
        ]

        labels = {
            "title": "Назва",
            "description": "Опис",
            "course": "Курс",
            "passing_score": "Прохідний бал (%)",
            "time_limit": "Обмеження часу (хв)",
            "status": "Статус",
        }

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }