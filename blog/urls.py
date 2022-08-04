from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogView.as_view(), name="home"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("create/", views.BlogCreateView.as_view(), name="create_blog"),
    path("edit/<int:pk>", views.BlogUpdateView.as_view(), name="update_blog"),
    path("delete/<int:pk>", views.BlogDeleteView.as_view(), name="delete_blog"),
]
