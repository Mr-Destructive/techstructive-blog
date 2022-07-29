from django.contrib import admin
from user.models import User
from articles.models import Article

admin.site.register(Article)
admin.site.register(User)
# Register your models here.
