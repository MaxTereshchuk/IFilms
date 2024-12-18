from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country = models.CharField(max_length=20, unique=False)
    favourite_movie = models.CharField(max_length=40, unique=False)
