from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import UserLoginForm,UserCreationForm
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('glavni'))
    else:
        form = UserLoginForm()

    users = User.objects.all()
    context = {'users':users,
               'form': form}
    return render(request,'main/login.html',context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
    context = {'users':form}
    return render(request, 'main/register.html',context)
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect(reverse('glavni'))