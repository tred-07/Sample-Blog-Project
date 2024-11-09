from django.shortcuts import render

# Create your views here.
def add_categories(request):
    return render(request,'add_category.html')