from django.shortcuts import render,redirect
from . import form
from . import models
# Create your views here.
def add_post(request):
    if request.method=='POST':
        form1=form.PostsForm(request.POST)
        form1.save()
        return redirect('home')
    return render(request,'add_post.html',{'form':form.PostsForm})



def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    form1=form.PostsForm(instance=post)
    if request.method=='POST':
        form1=form.PostsForm(request.POST,instance=post)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    return render(request,'add_post.html',{'form':form1})

def delete_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')