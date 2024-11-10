from django.shortcuts import render
from posts.models import Post
def home(request):
    posts=Post.objects.all()
    print(posts)
    for post in posts:
        for j in post.category.all():
            print(j)
    return render(request,'home.html',{'posts':posts})