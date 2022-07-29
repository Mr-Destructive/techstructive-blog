from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("delete/<int:pk>/", views.ArticleDetailView.as_view(), name="article-delete"),
    path("edit/<int:pk>", views.ArticleDetailView.as_view(), name="article-update"),
    #path("list/", TemplateView.as_view(template_name="articles/htmx_articlelist.html")),
]
