from django.urls import path
from .views import conduct_quiz,instructions


urlpatterns = [
    path(r'start', conduct_quiz, name='conduct_quiz'),
    path(r'instructions/<slug:quizid>', instructions, name='instructions'),
]