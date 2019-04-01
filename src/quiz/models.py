from django.db import models
from django.utils.timezone import now


# Model for Quiz
class Quiz(models.Model):
    # Quiz Credentials
    quiz_id = models.CharField(max_length=20, primary_key=True)
    quiz_name = models.CharField(max_length=100)
    quiz_password = models.CharField(max_length=50, null=False)

    # Quiz Duration
    quiz_time = models.DateTimeField(default=now)
    duration = models.IntegerField(default=120)  # Quiz duration in minutes

    # Quiz info
    description = models.TextField(max_length=400)
    instructions = models.TextField(max_length=400)

    # Automatic info
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.quiz_name

    class Meta:
        db_table = 'Quiz'
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


# Model for each question of a quiz
class Question(models.Model):

    TYPE = (
        ('s', 'Subjective Question'),
        ('m', 'Multiple Choice Single-Correct'),
        ('o', 'Multiple Choice Multi-Correct'),
    )

    LEVEL = (
        ('e', 'Easy'),
        ('m', 'Medium'),
        ('h', 'Hard'),
        ('d', 'Difficult'),
    )

    # Question info
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.TextField(max_length=1000, null=False)

    type = models.CharField(max_length=1, choices=TYPE, default='s')  # type of question as selected by admin
    marks = models.IntegerField(default=4)   # Marks for each Questions
    time_limit = models.IntegerField(default=3600)  # Time limit for each question default is set to 3 hours
    level = models.CharField(max_length=1, choices=LEVEL, default='m')  # Difficulty level for each question

    # Subjective Question
    max_words = models.IntegerField(default=1000)
    subjective_answer = models.TextField(max_length=1500, blank=True, default='')

    # Objective Options
    option_A = models.TextField(max_length=300,  blank=True, default='')
    option_B = models.TextField(max_length=300,  blank=True, default='')
    option_C = models.TextField(max_length=300,  blank=True, default='')
    option_D = models.TextField(max_length=300,  blank=True, default='')

    # Objective Correct
    correct = models.CharField(max_length=7, blank=True, default='')

    @property
    def is_subjective(self):
        return self.type == 's'

    @property
    def is_single(self):
        return self.type == 'o'

    @property
    def is_multiple(self):
        return self.type == 'm'

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'Questions'
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'







