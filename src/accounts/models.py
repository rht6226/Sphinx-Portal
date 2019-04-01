from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    registration_number = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, default='')
    profile_image = models.ImageField(null=True, blank=True, upload_to='users/')

    def get_full_name(self):
        # get the full name of the user
        return self.first_name + ' ' + self.last_name

    @property
    def image_url(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return r"https://res.cloudinary.com/dz2bsme0a/image/upload/v1548468434/user.png"

    def is_admin(self):
        if self.is_staff and self.is_superuser:
            return True
        return False

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
