from django.db import models
from questions.models import Question


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="Питання"
    )

    text = models.CharField(
        max_length=500,
        verbose_name="Відповідь"
    )

    is_correct = models.BooleanField(
        default=False,
        verbose_name="Правильна відповідь"
    )

    order = models.PositiveIntegerField(
        default=1,
        verbose_name="Порядок"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Відповідь"
        verbose_name_plural = "Відповіді"

    def __str__(self):
        return self.text