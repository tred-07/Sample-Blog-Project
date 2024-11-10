from django.shortcuts import render,redirect
from . import form
# Create your views here.
def add_post(request):
    if request.method=='POST':
        form1=form.PostsForm(request.POST)
        form1.save()
        return redirect('home')
    return render(request,'add_post.html',{'form':form.PostsForm})