from django.shortcuts import render, redirect
from .forms import PostForm


def post_creation_view (request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    return render(request, 'post/post_creation.html', {'form': form})
