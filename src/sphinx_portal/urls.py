"""sphinx_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from admin_panel.views import quiz_leader_board, leader_board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('super/', include('admin_panel.urls')),
    path('quiz/', include('quiz.urls')),
    path('leaderboard/', leader_board, name='general_board'),
    path('leaderboard/<slug:quiz_id>', quiz_leader_board, name='quiz_board'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
