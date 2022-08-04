from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create/", views.ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("delete/<int:pk>/", views.ArticleDetailView.as_view(), name="article-delete"),
    path("edit/<int:pk>", views.ArticleDetailView.as_view(), name="article-update"),
    #path("edit/<int:pk>/", views.ArticleUpdateView.as_view(), name="article-update"),
    path("meta/", views.ArticleMetaView.as_view(), name="article-meta"),
]
