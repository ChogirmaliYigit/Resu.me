from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(unique=True)
    job = models.CharField(max_length=1000, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='cover_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    social_media_link = models.URLField(verbose_name='Link:', max_length=255,null=True, blank=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        full_name = ''
        if self.first_name:
            full_name += self.first_name
        if self.last_name:
            full_name += f' {self.last_name}'
        if not full_name:
            full_name = self.username
        return full_name

    class Meta:
        db_table = 'users'
