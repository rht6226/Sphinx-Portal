from django import forms
from quiz.models import Quiz


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ('quiz_name', 'quiz_time', 'duration', 'description', 'instructions',
                  'tags')

        widgets ={
            'description': forms.Textarea(attrs={'class': 'form-control col-8'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control col-8'}),
            'quiz_name': forms.TextInput(attrs={'class': 'form-control col-6'}),
            # 'quiz_password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control col-6'}),
            'quiz_time': forms.DateTimeInput(attrs={'class': 'form-control col-4', 'placeholder': 'YYYY-MM-DD HH:MM'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control col-3', }),
            # 'quiz_id': forms.TextInput(attrs={'class': 'form-control col-6'}),
            'tags': forms.TextInput(attrs={'class': 'form-control col-6',
                                           'placeholder': 'Separate tags with semicolon (;)'}),
        }