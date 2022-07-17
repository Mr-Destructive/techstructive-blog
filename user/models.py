from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True


class Author(AbstractBaseUser):
    username = models.CharField(max_length=128)
    bio = models.TextField()
