from django.urls import path
from .views import create_quiz, add_questions, finish
from sphinx_portal import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'cook', create_quiz, name='create_quiz'),
    path('add_questions/<slug:quizid>', add_questions, name='add_questions'),
    path('finish', finish, name='finish')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)