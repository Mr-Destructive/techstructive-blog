from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
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
                    "style": "contenteditable='true'",
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
