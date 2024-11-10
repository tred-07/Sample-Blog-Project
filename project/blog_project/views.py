from django.shortcuts import render
from django import forms
from .blogForm import Blog
# Create your views here.

def BlogPage(request):
    return render(request,'blog.html',{'form':Blog})
