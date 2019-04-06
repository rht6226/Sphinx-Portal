from django.shortcuts import render
from django.contrib import auth, messages
from .models import Quiz, Question
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
        if (temp < timedelta(minutes=5)):
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

