from django.contrib import admin
from.models import Quiz, Question


class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'quiz_name', 'quiz_time', 'duration', 'is_active', 'quizmaster')
    list_filter = ('is_active', 'created_at', 'duration')
    fieldsets = (
        (None, {'fields': ('quiz_id', 'quiz_name', 'quiz_password')}),
        ('Quiz info', {'fields': ('quiz_time', 'duration', 'created_at', 'is_active')}),
        ('Quiz Description', {'fields': ('description', 'instructions', 'quizmaster', 'tags','users_appeared')}),
    )
    ordering = ('quiz_id', 'quiz_name', 'quiz_password', 'quiz_time', 'description', 'instructions')
    filter_horizontal = ()


class QuesAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question', 'marks', 'negative', 'time_limit', 'type', 'level')
    list_filter = ('quiz', 'level', 'type')
    fieldsets = (
        (None, {'fields': ('quiz', 'type', 'question', 'marks', 'negative', 'time_limit', 'level')}),
        ('Add Ons', {'fields': ('image', 'code')}),
        ('If Subjective', {'fields': ('max_words', 'subjective_answer')}),
        ('If Objective', {'fields': ('option_A', 'option_B', 'option_C', 'option_D', 'correct')}),
    )
    ordering = ('quiz', 'type', 'question', 'level', 'marks', 'negative', 'time_limit')
    filter_horizontal = ()


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuesAdmin)
