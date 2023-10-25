from django.shortcuts import render
from .models import Quiz, Question, Option
from django.views.generic import CreateView


class CreateQuiz(CreateView):
    model = Quiz
    fields = ['title', 'description', 'numberOfQuestions', 'duration', 'scheduledTime', 'additionalNote']
    template_name = 'host/createQuiz.html'
