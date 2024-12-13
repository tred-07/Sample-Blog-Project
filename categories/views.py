from django.shortcuts import render
from . import form
# Create your views here.
def add_categories(request):
    if request.method=='POST':
        form1=form.CategoryForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request,'add_category.html',{'form':form.CategoryForm})