from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email

# get the user model
User = get_user_model()


# Function for the home page
def home(request):
    return render(request, 'base.html', {'title': 'HOME'})


# Function to manage Authentication
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    # POST
    if request.method == 'POST':
        username = strip_tags(request.POST.get('username'))
        password = strip_tags(request.POST.get('password'))
        account = authenticate(username=username, password=password)

        if account is not None:
            print('user found... \n Now logging in')
            login(request, account)
            return redirect('home')

        else:
            print('Non existing user')
            message = "USER does not exists"
            context = {'title': 'Login', 'messages': [message]}
            return render(request, 'login.html', context=context)

    # GET
    else:
        context = {'title': 'Login'}
        return render(request, 'login.html', context=context)


# Function to logout the user
@login_required(login_url='/accounts/login/')
def logout_user(request):
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


