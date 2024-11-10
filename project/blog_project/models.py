from django.db import models
from author.models import Author 
from categories.models import Category
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=50)
    about=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)