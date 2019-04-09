from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question
from admin_panel.models import AnswerSheet, Answer
from datetime import datetime, date
from django.utils.timezone import datetime, timedelta

# Create your views here.


def conduct_quiz(request):
    return render(request,'conduct_quiz.html')


def instructions(request,quizid):

    try:
        item = Quiz.objects.get(quiz_id=quizid)
        user = request.user
        instruct = item.instructions
        instruct_list = instruct.split(";")
        today = datetime.now()
        temp = datetime.combine(date.min, today.time()) - datetime.combine(date.min, item.quiz_time.time())
        print(temp)
        if temp < timedelta(minutes=5):
            print("hola")
            margin = 1
        else:
            margin = 0

        return render(request, 'instructions.html',
                      {'quiz_object': item, 'user': user, 'instruct_list': instruct_list, 'today': today,
                       'margin': margin})
    except Quiz.DoesNotExist:
        messages.info(request, 'Quiz does not exists!')
        return redirect('dashboard')


@login_required()
def register_quiz(request, quizid):

    try:
        # Get Quiz form DB
        quiz_instance = Quiz.objects.get(quiz_id=quizid)
        user = request.user
        tags = quiz_instance.tags
        tags_list = tags.split(';')

        if request.method == 'POST':
            try:
                # Check if user is already registered for the quiz
                sheet_instance = AnswerSheet.objects.get(quiz=quiz_instance, contestant=user)
                messages.info(request, 'You have already registered for this quiz')
                return redirect('dashboard')

            except AnswerSheet.DoesNotExist:
                sheet_instance = AnswerSheet()

                sheet_instance.quiz = quiz_instance
                sheet_instance.contestant = user
                sheet_instance.is_valid = True

                sheet_instance.save()
                messages.info(request, 'Best of Luck!! You have been successfully registered.')
                return redirect('dashboard')

        # Get the page
        else:
            context = {'title': 'Register for Quiz', 'quiz': quiz_instance, 'user': user, 'tags': tags_list}

        return render(request, 'register_quiz.html', context=context)

    except Quiz.DoesNotExist:
        # No such quiz found in the database
        messages.info(request, 'Quiz does not exists')
        return redirect('dashboard')




