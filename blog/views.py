from .models import Blog
from articles.models import Article
from .serializers import BlogSerializer
from .forms import BlogForm
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogView(View, LoginRequiredMixin):
    model = Blog
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        context = {}
        blog = Blog.objects.filter(authors=request.user)
        context["blogs"] = blog
        context["articles"] = Article.objects.filter(blog=blog)
        return render(request, "blog/blog_login.html", context)

    def post(self, request, *args, **kwargs):
        context = {}
        blog_id = request.POST.get('blog')
        blog = Blog.objects.get(id=blog_id)
        articles = Article.objects.filter(blog=blog)
        context = {'blog': blog, 'articles': articles}
        return render(request, "base.html", context)


class BlogSecureView:

    model = Blog

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        return handler


class BlogListView(BlogView, ListView):
    """View to list all Blogs."""

    template_name = "blog/index.html"


class BlogDetailView(BlogSecureView, DetailView):
    """View to list the details for a Blog."""

    template_name = "blog/blog_detail.html"


class BlogCreateView(CreateView):
    """View to create a new Blog"""

    form_class = BlogForm
    template_name = "blog/create_blog.html"
    success_url = "/blog"

    def form_valid(self, form):
        form.instance.authors = self.request.user
        return super().form_valid(form)


class BlogUpdateView(BlogSecureView, UpdateView):
    """View to update an Blog"""

    form_class = BlogForm
    template_name = "blog/edit_blog.html"
    success_url = "/blog"


class BlogDeleteView(BlogSecureView, DeleteView):
    """View to delete an Blog"""

    template_name = "blog/delete_blog.html"
    success_url = "/blog"
