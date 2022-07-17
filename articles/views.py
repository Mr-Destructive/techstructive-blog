from .models import Article  
from .serializers import ArticleSerializer
from .forms import ArticleForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import mixins, viewsets
from rest_framework.views import APIView

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleView(APIView):
    model = Article
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        return context

class ArticleSecureView():

    model = Article

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        return handler

class ArticleListView(ArticleView, ListView):
    """View to list all Articles."""
    template_name = "articles/index.html"


class ArticleDetailView(ArticleSecureView, DetailView):
    """View to list the details from one article."""
    template_name = "articles/article_detail.html"


class ArticleCreateView(CreateView):
    """View to create a new Article"""

    form_class = ArticleForm
    template_name = "articles/create_article.html"
    success_url = "/article"


class ArticleUpdateView(ArticleSecureView, UpdateView):
    """View to update an Article"""

    form_class = ArticleForm
    template_name = "articles/edit_article.html"
    success_url = "/article"

class ArticleDeleteView(ArticleSecureView, DeleteView):
    """View to delete an Article"""

    template_name = "articles/delete_article.html"
    success_url = "/article"
