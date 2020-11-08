from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginuser(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homeview')
            else:
                messages.error(request, 'Invalid Username or password')
        else:
            messages.error(request, 'Invalid Username or password')
    else:
        form=AuthenticationForm()
    return render(request, 'session/login.html',{'form':form})
def logoutuser(request):
    logout(request)
    messages.success(request, "successfully logged out!")
    return redirect('homeview') 
from .forms import SignUpForm 
def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('session:login') 
    else:
        form=SignUpForm()
    return render(request, 'session/signup.html',{'form':form})       

