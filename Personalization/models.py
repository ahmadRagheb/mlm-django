from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import admin

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    timezone = models.CharField(max_length=50, default='Russia/Moscow')
    phone = models.CharField(max_length=20, default='+7')

admin.site.register(UserProfile)