from django.urls import path
from .views import create_quiz, add_questions, finish

urlpatterns = [
    path(r'cook', create_quiz, name='create_quiz'),
    path('add_questions/<slug:quizid>', add_questions, name='add_questions'),
    path('finish', finish, name='finish')
]