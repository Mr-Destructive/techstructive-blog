from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "articles"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="home"),
    path("<int:pk>", views.ArticleDetailView.as_view(), name="article_detail"),
    path("create/", views.ArticleCreateView.as_view(), name="create_article"),
    path("edit/<int:pk>", views.ArticleUpdateView.as_view(), name="update_article"),
    path("delete/<int:pk>", views.ArticleDeleteView.as_view(), name="delete_article"),
    path("list/", TemplateView.as_view(template_name="articles/htmx_articlelist.html")),
]
