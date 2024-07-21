from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def register_user(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             username = data.get('username')
#             age = data.get('age')
#             email = data.get('email')
#             password = data.get('password')
#             university = data.get('university')

#             user = User.objects.create_user(email=email, username=username, age=age, university=university, password=password)
            
#             return JsonResponse({'message': 'User registered successfully'}, status=201)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

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
    