from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from post.models import BlogPost
from .forms import RegistrationForm, LoginForm


def home_view (request):
    posts = BlogPost.objects.all()
    return render(request, 'home/home.html', {'posts': posts})


def register_view (request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    return render(request, 'home/register.html', {'form': form})


def login_view (request):
    user = request.user
    if user.is_authenticated: return redirect('home-page')

    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home-page')
    return render(request, 'home/login.html', {'form': form})


def logout_view (request):
    logout(request)
    return redirect('home-page')
