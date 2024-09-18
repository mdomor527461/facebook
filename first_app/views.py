from django.shortcuts import render
from . import forms
def home(request):
    if(request.method == 'POST'):
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.UserForm()
    return render(request,'home.html',{'form':form})

# Create your views here.
