from django.urls import path, include
from .views import home, login_user, register, logout_user, edit_profile, dash, destroy_prev_session, change_password, view_profile
from django.conf.urls.static import static
from sphinx_portal import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', home, name='home'),
    path(r'dashboard', dash, name='dashboard'),
    path(r'login', login_user, name='login'),
    path(r'logout', logout_user, name='logout'),
    path(r'register', register, name='register'),
    path(r'edit_profile', edit_profile, name='edit_profile'),
    path(r'view_profile', view_profile, name='view_profile'),
    path('login/remove_session', destroy_prev_session, name='destroy_prev_session'),
    path(r'password', change_password, name='change_password'),

    # Password Reset URLS
    path(r'password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path(r'password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)