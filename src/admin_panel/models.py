from django.db import models
from quiz.models import Quiz, Question
from accounts.models import User


class AnswerSheet(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    contestant = models.ForeignKey(User, on_delete=models.CASCADE)

    # Start and End-time of the quiz
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    # Use this field to make a request to the server and check time after each question submission
    current_time = models.DateTimeField(blank=True, null=True)

    # Use this flag to register/deregister a user
    is_valid = models.BooleanField(default=True)
    # Use this flag to check if the candidate has already appeared in the test
    is_attempted = models.BooleanField(default=False)
    # Use this flag to check if the AnswerSheet has been graded
    is_graded = models.BooleanField(default=False)

    # Marks analysis
    total_marks_obtained = models.IntegerField(blank=True, null=True)
    total_subjective_marks = models.IntegerField(blank=True, null=True)
    total_objective_positive = models.IntegerField(blank=True, null=True)
    total_objective_negative = models.IntegerField(blank=True, null=True)
    total_marks_available = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.quiz.quiz_id, self.contestant.username)

    class Meta:
        db_table = 'AnswerSheets'
        verbose_name = 'AnswerSheet'
        verbose_name_plural = "AnswerSheets"

    def is_acceptable(self):
        return self.is_attempted and self.is_valid


class Answer(models.Model):
    sheet = models.ForeignKey(AnswerSheet, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    marks_awarded = models.IntegerField(default=0)

    # Question wise time
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # Subjective
    subjective_answer = models.TextField(null=True, blank=True, default='')

    # Objective Answers
    response_A = models.TextField(null=True, blank=True, default='')
    response_B = models.TextField(null=True, blank=True, default='')
    response_C = models.TextField(null=True, blank=True, default='')
    response_D = models.TextField(null=True, blank=True, default='')

    # Flag to ensure that an answer cannot be attempted twice
    is_attempted = models.BooleanField(default=False)
    # Flag to check if the sheet has been graded
    is_graded = models.BooleanField(default=False)

    def __str__(self):
        return "{}-QID-{}-{}".format(self.sheet.quiz.quiz_id, self.question.id, self.sheet.contestant.username)

    class Meta:
        db_table = 'Answer'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'



