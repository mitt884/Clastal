from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms


def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # if request.cleaned_data['remember_me'] == True:
            #     request.session.set_expiry(0)
            messages.success(request, ("ログインに成功しました"))
            return redirect('home')
        else:
            messages.success(request, ("無効な資格情報"))
            return redirect('login')
    else:
        return render(request, 'register.html', {})

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # if request.cleaned_data['remember_me'] == True:
            #     request.session.set_expiry(0)
            messages.success(request, ("ログインに成功しました"))
            return redirect('home')
        else:
            messages.success(request, ("無効な資格情報"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('home')
    