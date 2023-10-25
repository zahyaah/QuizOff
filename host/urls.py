from django.urls import path
from .views import CreateQuiz


urlpatterns = [
    path('create-quiz/', CreateQuiz.as_view(), name='create_quiz')
]


