from django import forms
from . import models
from categories.models import Category
from author.models import Author
class PostsForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields='__all__'