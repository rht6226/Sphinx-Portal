from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import QuizForm
from django.contrib import auth, messages
from django.core.mail import send_mail
from quiz.models import Quiz, Question
import socket
socket.getaddrinfo('localhost', 8000)


def finish(request):
    return render(request, 'dashboard.html')


def add_questions(request, quizid):

    user = request.user
    if user.is_admin():

      quiz = Quiz.objects.get(quiz_id=quizid)

      if request.method == 'POST':

          type = request.POST.get('type')
          ques = Question()
          ques.quiz= quiz
          ques.type = request.POST.get('type')
          ques.marks = request.POST.get('marks')
          ques.level = request.POST.get('level')
          ques.time_limit = request.POST.get('time_limit')
          ques.question = request.POST.get('question')
          print(ques.level)

          if type=='s':
              ques.subjective_answer = request.POST.get('subjective_answer')
              ques.save()
          else:
              ques.option_A = request.POST.get('option_a')
              ques.option_B = request.POST.get('option_b')
              ques.option_C = request.POST.get('option_c')
              ques.option_D = request.POST.get('option_d')
              ques.correct = request.POST.get('correct')
              ques.save()
          return JsonResponse({'kudos':"kudos"})

      else:
          return render(request, 'add_questions.html', {'quiz_data':quiz})
    else:

        messages.info(request, 'You do not have the permissions required to edit this quiz')
        return redirect('home')


def create_quiz(request):

    user = request.user
    if user.is_admin():
        if request.method == 'POST':
            # form is submitted
            quiz_form = QuizForm(request.POST, request.user)
            if quiz_form.is_valid:
                item = Quiz()
                try:
                    qu = Quiz.objects.get(quiz_id=request.POST['quiz_id'])
                    create_quiz_form = QuizForm()
                    return render(request, 'create_quiz.html',
                                  {'quiz_form': create_quiz_form, 'error': "Quiz id is already taken! "})
                except Quiz.DoesNotExist:
                    item.quiz_name = request.POST['quiz_name']
                    item.description = request.POST['description']
                    item.quiz_id = request.POST['quiz_id']
                    item.quiz_password = request.POST['quiz_password']
                    item.instructions = request.POST['instructions']
                    item.duration = request.POST['duration']
                    item.quiz_time = request.POST['quiz_time']
                    item.quizmaster = request.user
                    item.tags = request.POST['tags']
                    item.save()
                    send_mail(
                        'New Quiz Created',
                        'Here is the message.',
                        'binary.compatible@gmail.com',
                        ['ojha.ashwini.1998@gmail.com'],
                        fail_silently=False,
                    )
                    return redirect('add_questions/'+item.quiz_id)
            else:
                messages.error(request, 'Please correct the error below.')
                return render(request, 'create_quiz.html', {'quiz_form': create_quiz_form})

        else:
            # get request. We have to return the form so that user can fill it.
            create_quiz_form = QuizForm()
            return render(request, 'create_quiz.html', {'quiz_form': create_quiz_form})
    else:
        messages.info(request, 'You do not have the permissions required create a quiz')
        return redirect('home')
