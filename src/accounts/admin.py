from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
from django.contrib.auth.models import Permission


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'registration_number')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'registration_number')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio', 'profile_image')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    ordering = ('username', 'email', 'first_name', 'last_name', 'registration_number')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.unregister(Group)
