from django.db import models
from categories.models import Categories
from author.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Categories)
    author=models.OneToOneField(Author)
