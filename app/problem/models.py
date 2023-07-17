from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, primary_key=True, default="general")


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

    tags = models.ManyToManyField(
        Tag, through="TPjoin", related_name='problem_set', through_fields=('problem', 'tag'))


class TPjoin(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, to_field='name', on_delete=models.CASCADE)
