from django.urls import path
from .views import conduct_quiz, instructions, register_quiz


urlpatterns = [
    path(r'start', conduct_quiz, name='conduct_quiz'),
    path(r'register_quiz/<slug:quizid>', register_quiz, name='register_quiz'),
    path(r'instructions/<slug:quizid>', instructions, name='instructions'),
]