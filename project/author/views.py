from django.shortcuts import render
from . import models
# Create your views here.
def add_authors(request):
    form=models.Author()
    return render(request,'add_author.html',{'form':form})