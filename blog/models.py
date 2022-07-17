from django.db import models
from user.models import Author


class Blog(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
