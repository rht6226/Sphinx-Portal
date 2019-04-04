from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import QuizForm
from django.contrib import auth, messages
from django.utils.html import strip_tags
from django.core.mail import send_mail
from quiz.models import Quiz, Question
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import socket
import random
socket.getaddrinfo('localhost', 8000)


def finish(request):
    return render(request, 'dashboard.html')


def add_questions(request, quizid):

    user = request.user
    if user.is_admin():

        quiz = Quiz.objects.get(quiz_id=quizid)

        if request.method == 'POST':

            q_type = strip_tags(request.POST.get('type'))
            ques = Question()
            ques.quiz = quiz
            ques.type = strip_tags(request.POST.get('type'))
            ques.marks = strip_tags(request.POST.get('marks'))
            ques.level = strip_tags(request.POST.get('level'))
            ques.time_limit = strip_tags(request.POST.get('time_limit'))
            ques.question = strip_tags(request.POST.get('question'))


            # if Image is uploaded
            img = request.FILES.get('image')
            if img:

                ques.image = img
            else:
                print("\n\n\n\nNo File was uploaded\n\n\n\n")

            # if Code is added
            code = request.POST.get('code')
            if code:
                ques.code = code

            # if Question is subjective
            if q_type == 's':
                ques.subjective_answer = strip_tags(request.POST.get('subjective_answer'))

            # Question is objective
            else:
                ques.option_A = strip_tags(request.POST.get('option_a'))
                ques.option_B = strip_tags(request.POST.get('option_b'))
                ques.option_C = strip_tags(request.POST.get('option_c'))
                ques.option_D = strip_tags(request.POST.get('option_d'))
                ques.correct = strip_tags(request.POST.get('correct'))

            ques.save()
            return JsonResponse({'kudos': "kudos"})

        # GET the page
        else:
            return render(request, 'add_questions.html', {'title': 'Add Questions', 'quiz_data': quiz})
    # User Does not has sufficient permissions
    else:

        messages.info(request, 'You do not have the permissions required to edit this quiz')
        return redirect('home')


# This function creates a unique ID for new quiz
def create_quiz_id(size):
    uid = get_random_string(length=size)

    # check if Quiz already exists if not, return id
    try:
        notebook = Quiz.objects.get(quiz_id=uid)
    except:
        notebook = None

    if not notebook:
        return uid
    else:
        create_quiz_id(size)  # If uid already exists recreate uid


@login_required(login_url='/accounts/login/')
def create_quiz(request):

    user = request.user
    if user.is_admin():

        if request.method == 'POST':
            # form is submitted
            quiz_form = QuizForm(request.POST, request.user)

            if quiz_form.is_valid:
                # Create new instance of quiz
                item = Quiz()

                # Create random id and password
                item.quiz_id = create_quiz_id(size=random.randint(5, 10))
                item.quiz_password = get_random_string(length=random.randint(8, 12))

                # Fill other details of the Quiz Object
                item.quiz_name = strip_tags(request.POST['quiz_name'])
                item.description = strip_tags(request.POST['description'])
                item.instructions = strip_tags(request.POST['instructions'])
                item.duration = strip_tags(request.POST['duration'])
                item.quiz_time = request.POST['quiz_time']
                item.quizmaster = request.user
                item.tags = strip_tags(request.POST['tags'])

                # Save the Quiz object and mail the credentials
                item.save()
                send_mail(
                    'New Quiz Created',
                    'Here is the message.',
                    'binary.compatible@gmail.com',
                    ['ojha.ashwini.1998@gmail.com'],
                    fail_silently=True,
                )
                return redirect('add_questions/'+item.quiz_id)
            # errors are raised
            else:
                messages.error(request, 'Please correct the error below.')
                return render(request, 'create_quiz.html', {'title': 'Create Quiz', 'quiz_form': quiz_form})

        else:
            # get request. We have to return the form so that user can fill it.
            create_quiz_form = QuizForm()
            return render(request, 'create_quiz.html', {'title': 'Create Quiz', 'quiz_form': create_quiz_form})
    else:
        messages.info(request, 'You do not have the permissions required create a quiz')
        return redirect('home')
