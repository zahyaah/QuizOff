from django.db import models
from host.models import Quiz, Question, Option
from django.core import validators


class Participant(models.Model):
    username = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[validators.EmailValidator(message="Invalid Email")], null=True, blank=True)

    def __str__(self):
        return self.name


class Response(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selectedOption = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.question + " " + self.selectedOption
