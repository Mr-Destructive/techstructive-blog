from django.db import models
from user.models import User


class Blog(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name="authors")
