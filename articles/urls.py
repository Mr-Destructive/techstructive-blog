from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("delete/<int:pk>/", views.ArticleDetailView.as_view(), name="article-delete"),
    #path("edit/<int:pk>", views.ArticleDetailView.as_view(), name="article-update"),
    path("edit/<int:pk>/", views.ArticleUpdateView.as_view(), name="article-update"),
]
