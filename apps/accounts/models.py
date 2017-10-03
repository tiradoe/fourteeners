from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    location = models.CharField(max_length=255)
    picture = models.ImageField(default=None, blank=True, upload_to='media')

    next_mountain1 = models.CharField(max_length=50)
    next_mountain2 = models.CharField(max_length=50)
    next_mountain3 = models.CharField(max_length=50)
    next_mountain4 = models.CharField(max_length=50)
    next_mountain5 = models.CharField(max_length=50)


class settings(models.Model):
    user = models.OneToOneField(User)
