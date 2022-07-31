from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views import View
import frontmatter
from django.shortcuts import redirect


from .models import Article
from .forms import ArticleForm


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

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
        return render(request, "articles/partials/article-list.html", {'articles': articles})
    
    def put(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id=pk)
        form = ArticleForm(instance=article, data=QueryDict(request.body))
        if form.is_valid():
            article = form.save()
            return render(self.request, "articles/partials/article-detail.html", {'article': article})

    def post(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id=pk)
        form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/partials/update.html', context)

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/edit_article.html"

class ArticleMetaView(View):
    model = Article

    def post(self, request, *args, **kwargs):
        import json
        data = json.loads(json.dumps(dict(request.POST)))
        loaded_frontmatter = frontmatter.loads(data['content'][0])
        if dict(loaded_frontmatter):
            article_title = loaded_frontmatter['title']
            article_description = loaded_frontmatter['description']
            form = ArticleForm(initial={'title': article_title, 'description': article_description, 'content': loaded_frontmatter.content})
            context = {'form': form}
            if Article.objects.filter(title=article_title):
                article = Article.objects.filter(title=article_title).last()
                context['article'] = article
                return render(request, 'articles/edit_article.html', context)
            return render(request, 'articles/article_form.html', context)
        article_list = Article.objects.filter(title=data['title'][0])
        if article_list:
            article = article_list.last()
            form = ArticleForm(data=request.POST)
            context = {'form': form}
            context['article'] = article
            return render(request, 'articles/edit_article.html', context)
        form = ArticleForm(initial={'content': data['content'][0]})
        context = {'form': form}
        return render(request, 'articles/article_form.html', context)
