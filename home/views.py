from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from post.models import BlogPost, BlogImage, BlogVideo, BlogAudio
from .forms import RegistrationForm, LoginForm


def home_view(request):
    posts = BlogPost.objects.all()
    posts_list = []
    for post in posts:
        is_image = False
        is_video = False
        is_audio = False
        images = BlogImage.objects.filter(blog_post = post)

        # Taking first image as a headliner
        if images:
            image = images[0]
            is_image = True
        else:
            image = None

        if BlogVideo.objects.filter(blog_post = post):
            is_video = True
        if BlogAudio.objects.filter(blog_post = post):
            is_audio = True

        id = post.id
        name = post.name
        date = post.date
        content = post.content
        if len(content) > 800:
            content = content[:800] + '...'

        posts_list.append({'name': name,
                           'date': date,
                           'content': content,
                           'image': image,
                           'is_image': True,
                           'is_video': True,
                           'is_audio': True,
                           'id': id})

    return render(request, 'home/home.html', {'posts': posts_list})


def register_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    return render(request, 'home/register.html', {'form': form})


def login_view(request):
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


def logout_view(request):
    logout(request)
    return redirect('home-page')
