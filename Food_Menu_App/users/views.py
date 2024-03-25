from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, RegisterationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    error_message = None  # Initialize an error message variable
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('food:index')
        else:
            error_message = "Invalid username or password. Please ty again."

    return render(request, 'users/login.html', {'error_message': error_message})

def register_view(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('food:index')
    else:
        form = RegisterationForm()
    return render(request, 'users/register.html', {'form':form})
            

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
