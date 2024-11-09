from django.shortcuts import render,redirect
from . import form
# Create your views here.
def add_authors(request):
    if request.method=='POST':
       form1=form.AuthorForm(request.POST)
       if form1.is_valid:
            form1.save()
            print("Ok")
            return render(request,'add_author.html',{'form':form1})
    return render(request,'add_author.html',{'form':form.AuthorForm()})

def confAuthor(request):
        pass