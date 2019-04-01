from django.urls import path
from .views import home, login_user, register, logout_user

urlpatterns = [
    path(r'', home, name='home'),
    path(r'login', login_user, name='login'),
    path(r'logout', logout_user, name='logout'),
    path(r'register', register, name='register'),
]