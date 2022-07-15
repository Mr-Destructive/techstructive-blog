from user.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.db import models

class Tags(TimeStampedModel):
    ...

class Series(TimeStampedModel):
    ...

class Author(TimeStampedModel):
    ...

class Article(TimeStampedModel):

    class Article_Status(models.TextChoices): 
        DRAFT = 'DRAFT', _('Draft'),
        PUBLISHED = 'PUBLISHED', _('Published'),

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.TextField(default="", null=False, blank=False)
    status = models.CharField(
            max_length=16,
            choices=Article_Status.choices,
            default=Article_Status.DRAFT,
    )

