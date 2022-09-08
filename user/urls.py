from django.urls import path

from user.views import (
    register,
)

app_name = "user"
urlpatterns = [
    path("register/", view=register, name='register'),
]
