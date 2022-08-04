from django import forms
from blog.models import Blog
from .models import Article


class ArticleForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(authors=user)

    class Meta:
        model = Article
        exclude = (
            "created",
            "updated",
            "author",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 450px; align: center;",
                    "placeholder": "Title",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 900px; ",
                    "placeholder": "Description",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control post-body",
                    "id": "text-content",
                    "style": "max-width:900px;",
                    "hx-post": "/article/meta/",
                    "placeholder": "Content",
                }
            ),
            "blog": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Blog Publication",
                }
            ),
        }
