from django.shortcuts import render,redirect
from . import form
def add_profiles(request):
    if request.method=='POST':
       form1=form.ProfileForm(request.POST)
       if form1.is_valid():
           form1.save()
           return redirect('home')
    return render(request,'add-profiles.html',{'form':form.ProfileForm})