from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=100)
    statement = models.TextField()

    class Difficulty(models.TextChoices):
        EASY = "Easy",
        MED = "Medium",
        HARD = "Hard",

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )
