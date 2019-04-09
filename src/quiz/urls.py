from django.urls import path
from .views import conduct_quiz, instructions, register_quiz, quiz_auth


urlpatterns = [
    path(r'start', conduct_quiz, name='conduct_quiz'),
    path(r'register_quiz/<slug:quizid>', register_quiz, name='register_quiz'),
    path(r'instructions/<slug:quizid>', instructions, name='instructions'),
    path(r'start_quiz/test/<slug:quizid>', conduct_quiz, name='conduct_quiz'),
    path('start_quiz/<slug:quizid>', quiz_auth, name='quiz_auth'),
]