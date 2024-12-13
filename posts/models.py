from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100,default=None)
    content=models.TextField()
    category=models.ManyToManyField(Category,default=None)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.title


    