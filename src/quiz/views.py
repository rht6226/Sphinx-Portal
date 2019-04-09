from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question
from admin_panel.models import AnswerSheet, Answer
from django.utils.html import strip_tags
from datetime import datetime, date
from django.utils.timezone import datetime, timedelta

# Create your views here.


@login_required()
def quiz_auth(request, quizid):

    item = Quiz.objects.get(quiz_id=quizid)
    item.duration = item.duration
    users = item.users_appeared.filter(pk=request.user.pk)

    if users.exists():
        messages.info(request, 'You already appeared in this Quiz')
        return redirect('dashboard')
    else:
        if item.quiz_password == request.POST['password']:
            request.session['username'] = quizid
            # if request.user.profile.role == 'client':
            #     item.users_appeared.add(request.user)

            return redirect('test/' + str(quizid))
        else:

            # return render(request, 'start', {'error': 'Invalid Credentials!'})
            messages.info(request, 'Invalid Credentials')
            return redirect('dashboard')


def create_answer_table(quiz_object, question_objects, user_object):
    for question_object in question_objects:
        list_sheet = get_object_or_404(AnswerSheet, contestant=user_object, quiz=quiz_object)
        ans = Answer()
        ans.sheet = list_sheet
        ans.question = question_object
        ans.save()
    return


# Function for conducting quiz
def conduct_quiz(request, quizid):

    aspirant = request.user
    item = get_object_or_404(Quiz, quiz_id=quizid)
    data = Question.objects.filter(quiz=item)
    list_sheet = get_object_or_404(AnswerSheet, contestant=aspirant, quiz=item)

    # Question Submission
    if request.method == 'POST':
        if list_sheet.is_valid and not list_sheet.is_attempted:
            question_object = get_object_or_404(Question, id=request.POST.get('question_id'))
            answer_object = get_object_or_404(Answer, question=question_object, sheet=list_sheet)

            if not answer_object.is_attempted:
                # Update values
                if question_object.is_subjective:
                    answer_object.subjective_answer = strip_tags(request.POST.get('subjective_answer'))
                elif question_object.is_single:
                    answer_object.response_A = request.POST.get('single_answer')

                # Multi correct
                else:
                    check_list = request.POST.getlist('multi_answer[]')
                    print(check_list[0])
                    length = len(check_list)
                    if length == 1:
                        answer_object.response_A = check_list[0]
                    elif length == 2:
                        answer_object.response_A = check_list[0]
                        answer_object.response_B = check_list[1]
                    elif length == 3:
                        answer_object.response_A = check_list[0]
                        answer_object.response_B = check_list[1]
                        answer_object.response_C = check_list[2]
                    elif length == 4:
                        answer_object.response_A = check_list[0]
                        answer_object.response_B = check_list[1]
                        answer_object.response_C = check_list[2]
                        answer_object.response_D = check_list[3]

                answer_object.is_attempted = True
                answer_object.save()

            else:
                context = {'title': 'Error', 'messages': 'You have already attempted this question'}
                return JsonResponse(context)

        else:
            messages.info(request, 'You have already attempted this quiz')
            return redirect('dashboard')

    querys = []
    for question in data:
        querys.append(question)

    else:
        try:
            answers = get_list_or_404(Answer, sheet=list_sheet)
        except:
            create_answer_table(item, data, aspirant)

    return render(request, 'conduct_quiz.html', {'title': 'Best of Luck', 'quiz_object': item, 'quiz_data': querys,
                                                 'user': aspirant})


@login_required()
def instructions(request, quizid):

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
        # this is to check if the user has registered or not
        list_sheet = AnswerSheet.objects.filter(contestant=user).filter(quiz=quiz_instance)

        if list_sheet.exists():
            flag = 0
        else:
            flag = 1
        print(list_sheet)
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
            context = {'title': 'Register for Quiz', 'quiz': quiz_instance, 'user': user, 'tags': tags_list, 'flag': flag}

        return render(request, 'register_quiz.html', context=context)

    except Quiz.DoesNotExist:
        # No such quiz found in the database
        messages.info(request, 'Quiz does not exists')
        return redirect('dashboard')




