from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views import View

from django.shortcuts import redirect

import articles

from .models import Article
from .forms import ArticleForm

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    #fields = ['title', 'description', 'content', 'status', 'blog']

    def form_valid(self, form):
        form.instance.author = self.request.user
        obj = form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Your article has been saved!')
        return render(self.request, "articles/partials/article-detail.html",{'article': obj})
        #return redirect("articles:article-detail", pk=obj.id)

class HomeView(ListView):
    model = Article
    template_name = "articles/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        articles = Article.objects.all()
        return super().get_context_data(articles=articles, **kwargs)

class ArticleDetailView(View):
    model = Article

    def get(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id=pk)
        return render(self.request, 'articles/article_detail.html', {'article': article})

    def delete(self, request, pk, *args, **kwargs):
        Article.objects.get(id=pk).delete()
        articles = Article.objects.filter(author=self.request.user)
        return HttpResponse("")
    
    def put(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id=pk)
        return render(self.request, 'articles/partials/update.html', {'form': ArticleForm(instance=article), 'article': article})
