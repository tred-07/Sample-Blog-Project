from django.shortcuts import render

# Create your views here.
def add_post(request):
    return render(request,'add_post.html')