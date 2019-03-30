from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html', {'title': 'HOME'})

def login(request):
    return render(request, 'login.html', {'title': 'Login'})

def register(request):
    return render(request, 'register.html', {'title':'Regitser'})
