from .models import Blog
from .serializers import BlogSerializer
from .forms import BlogForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import mixins, viewsets
from rest_framework.views import APIView


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogView(APIView):
    model = Blog
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        return context


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


class BlogUpdateView(BlogSecureView, UpdateView):
    """View to update an Blog"""

    form_class = BlogForm
    template_name = "blog/edit_blog.html"
    success_url = "/blog"


class BlogDeleteView(BlogSecureView, DeleteView):
    """View to delete an Blog"""

    template_name = "blog/delete_blog.html"
    success_url = "/blog"
