from django import forms
from categories.models import Category
from author.models import Author

class Blog(forms.ModelForm):
    class Meta:
        field='__all__'