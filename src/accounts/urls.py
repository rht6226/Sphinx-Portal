from django.urls import path
from .views import home, login_user, register, logout_user, edit_profile, dash, destroy_prev_session
from django.conf.urls.static import static
from sphinx_portal import settings

urlpatterns = [
    path(r'', home, name='home'),
    path(r'dashboard', dash, name='dashboard'),
    path(r'login', login_user, name='login'),
    path(r'logout', logout_user, name='logout'),
    path(r'register', register, name='register'),
    path(r'edit_profile', edit_profile, name='edit_profile'),
    path('login/remove_session', destroy_prev_session, name='destroy_prev_session'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)