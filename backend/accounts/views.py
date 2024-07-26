from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm, ChangeUserPassword

def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Use 'password1' for setting password
            user.save()
            messages.success(request, "登録に成功。ログインしてください登録に成功。ログインしてください")
            return redirect('login')  # Redirect to the login page
        else:
            # Render the form with errors instead of redirecting
            messages.error(request, "無効な資格情報")
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegisterForm()  # Initialize form for GET request
        return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
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
 
@login_required   
def update_user(request):
    current_user = request.user
    user_form = UserUpdateForm(request.POST or None, instance=current_user)

    if user_form.is_valid():
        user_form.save()
        messages.success(request, ("Update infos successfully"))
        return redirect('home')
    
    
    return render(request, 'update_user.html', {'user_form': user_form})

@login_required 
def update_password(request):
    current_user = request.user
    if request.method == 'POST':
        form = ChangeUserPassword(current_user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Password Successfully")
            return redirect('login')
        else:
            return redirect('update_password')
    else:
        form = ChangeUserPassword(current_user)
        return render(request, 'update_password.html', {'form': form})
    