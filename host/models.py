from django.db import models
from ckeditor.fields import RichTextField
from uuid import uuid4


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    numberOfQuestions = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default=uuid4, editable=False, unique=True)
    duration = models.DateTimeField()
    scheduledTime = models.DateTimeField()
    additionalNote = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question = RichTextField()  # Requires RichField

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    option = RichTextField()  # Requires RichTextField
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.option
