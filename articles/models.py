from user.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.db import models
from blog.models import Blog
from user.models import User


class Tags(TimeStampedModel):
    ...


class Series(TimeStampedModel):
    ...


class Article(TimeStampedModel):
    class Article_Status(models.TextChoices):
        DRAFT = (
            "DRAFT",
            _("Draft"),
        )
        PUBLISHED = (
            "PUBLISHED",
            _("Published"),
        )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.TextField(default="", null=False, blank=False)
    status = models.CharField(
        max_length=16,
        choices=Article_Status.choices,
        default=Article_Status.DRAFT,
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.title
