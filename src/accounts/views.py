from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from quiz.models import Quiz
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import os
from sphinx_portal import settings
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# get the user model
User = get_user_model()


def destroy_prev_session(request):
    user = User.objects.get(username=request.POST['username'])
    user.flag = False
    user.save()
    # The below line disables the user in order to login properly this must be set back again to true
    user.is_active = False
    user.save()

    return render(request, 'base.html', {'title': 'HOME'})


# Function for the home page
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard') if not request.user.is_admin() else redirect('admin_dashboard')
    else:
        return render(request, 'base.html', {'title': 'HOME'})


@login_required(login_url='/accounts/login')
def dash(request):

    item = Quiz.objects.all().order_by('quiz_name')
    paginator = Paginator(item, 5)  # Show 1o quizzes per page
    page = request.GET.get('page', 1)
    try:
        item = paginator.get_page(page)
    except PageNotAnInteger:
        item = paginator.get_page(1)
    except EmptyPage:
        item = paginator.get_page(paginator.num_pages)

    return render(request, 'dashboard.html', {'title': 'dashboard', 'quiz_object': item})


# Function to manage Authentication
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    # POST
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            username = strip_tags(request.POST.get('username'))
            password = strip_tags(request.POST.get('password'))

            if user.is_active == False:
                user.is_active = True
                user.save()

            account = authenticate(username=username, password=password)

            if account is not None:
                if user.flag == True:
                    return render(request, 'session_prevent.html', {'userroot': user.username})
                else:
                    user.flag=True
                    user.save()
                    print('user found... \n Now logging in')
                    login(request, account)
                    if request.user.is_admin():
                        return redirect('admin_dashboard')
                    else:
                        return redirect('dashboard')

            else:
                print('Non existing user')
                message = "USER does not exists"
                context = {'title': 'Login', 'messages': [message]}
                return render(request, 'login.html', context=context)
        except User.DoesNotExist:
            return render(request, 'login.html',
                          {'messages': 'Invalid Credentials! Please enter correct username and password.'})

    # GET
    else:
        context = {'title': 'Login'}
        return render(request, 'login.html', context=context)


# Function to logout the user
@login_required(login_url='/accounts/login/')
def logout_user(request):
    user = request.user
    user.flag = False
    user.save()
    logout(request)
    response = redirect('home')
    return response


# Function for managing registration
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    # POST
    if request.method == 'POST':

        # clean data
        username = strip_tags(request.POST.get('username'))
        password = strip_tags(request.POST.get('password1'))
        conf_password = strip_tags(request.POST.get('password2'))
        first_name = strip_tags(request.POST.get('first_name'))
        last_name = strip_tags(request.POST.get('last_name'))
        email = strip_tags(request.POST.get('email'))

        error_msg = []

        # check if passwords are identical; if not, raise error
        if password == conf_password:
            pass
        else:
            error_msg.append('Passwords do not match')

        # check if email is valid; if not, raise error
        if email:
            if validate_email(email) is None:
                print(validate_email(email))
                pass
            else:
                print('email err')
                error_msg.append('Invalid email')
        else:
            error_msg.append('kindly enter email')

        # check if username is taken and Email are taken
        try:
            user_with_username = User.objects.get(username=username)
        except:
            user_with_username = None
        if user_with_username:
            error_msg.append('Username Already Taken !')

        # check if email is taken
        try:
            user_with_mail = User.objects.get(email=email)
        except:
            user_with_mail = None
        if user_with_mail:
            error_msg.append('Email Already exists!')

        context = {'title': 'Error', 'messages': error_msg}

        # if error is raised redirect to home
        if error_msg:
            return render(request, 'register.html', context=context)

        # If No error was raised, Create User
        else:
            try:
                user = User.objects.create(username=username, email=email, first_name=first_name,
                                           last_name=last_name)
                print('user created')
                user.set_password(password)
                user.save()
                return render(request, 'register.html', context={'title': 'Home',
                                                                 'messages': ['user created successfully',
                                                                              'Login to continue']})
            except Exception as e:
                print(e)
                return render(request, 'register.html', context={'title': 'Home', 'messages': e})
    # GET
    else:
        return render(request, 'register.html', context={'title': 'Register'})


# Function for editing profile
@login_required(login_url='/login/')
def edit_profile(request):
    user = request.user
    user_instance = User.objects.get(username=user.username)
    context = {'title': 'Edit Profile', 'user': user_instance, "edit_page": "active"}

    if request.method == 'POST':

        if request.FILES.get('image'):  # Delete previous and rename image

            if user_instance.profile_image:     # Delete previous image. Make profile_image None
                os.remove(os.path.join(settings.MEDIA_ROOT, user_instance.profile_image.name))
                user_instance.profile_image = None
                user_instance.save()
                print('Deleted Previous image. \n Now saving new')

            format_name = request.FILES.get('image').name.split('.')
            request.FILES.get('image').name = "{}.{}".format(user.username,  format_name[1])    # Rename Uploaded file
            user_instance.profile_image = request.FILES.get('image')
            user_instance.save()
            return redirect('edit_profile')

        else:
            user_instance.first_name = request.POST.get('first_name')
            user_instance.last_name = request.POST.get('last_name')
            user_instance.registration_number = request.POST.get('registration_number')
            user_instance.bio = request.POST.get('bio') if request.POST.get('bio') else user.bio
            user_instance.save()
            return redirect('edit_profile')

        # else:
        #     return HttpResponse('Sorry! Something went wrong.')

    else:
        return render(request, 'edit_profile.html', context=context)


# Change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form, 'title': 'Change Password'
    })
