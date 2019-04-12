from django.urls import path
from .views import conduct_quiz, instructions, register_quiz, quiz_auth, end_quiz, start_quiz
from sphinx_portal import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'start', conduct_quiz, name='conduct_quiz'),
    path(r'register_quiz/<slug:quizid>', register_quiz, name='register_quiz'),
    path(r'instructions/<slug:quizid>', instructions, name='instructions'),
    path(r'start_quiz', start_quiz, name='start_quiz'),
    path(r'start_quiz/test/<slug:quizid>', conduct_quiz, name='conduct_quiz'),
    path(r'start_quiz/<slug:quizid>', quiz_auth, name='quiz_auth'),
    path(r'the_end/<slug:quizid>', end_quiz, name='end_test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)