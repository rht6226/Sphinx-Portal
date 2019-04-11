from django.urls import path
from .views import create_quiz, add_questions, finish, admin_dash, edit_quiz, grader, sheet_grader, finish_grading
from sphinx_portal import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', admin_dash, name='admin_dashboard'),
    path(r'cook', create_quiz, name='create_quiz'),
    path(r'edit/<slug:quizid>', edit_quiz, name='edit_quiz'),
    path(r'add_questions/<slug:quizid>', add_questions, name='add_questions'),
    path(r'grade/<slug:quizid>', grader, name='grader'),    # URL for all AnswerSheets to be graded
    path(r'grade/sheet/<slug:sheet_id>', sheet_grader, name='sheet_grader'),    # URL for grading the answers in a sheet
    path(r'grade/sheet/<slug:sheet_id>/finish', finish_grading, name='finish_grade'),    # Finish Grading and add score
    path(r'finish', finish, name='finish')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)