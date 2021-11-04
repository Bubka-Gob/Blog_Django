from django.shortcuts import render, redirect
from .forms import PostForm
from .models import BlogPost, BlogImage


def post_creation_view (request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = BlogPost(name=form.data['name'], content=form.data['content'])
            blog_post.save()
            for image in form.files.getlist('images'):
                image_post = BlogImage(image=image, blog_post=blog_post)
                image_post.save()
            return redirect('home-page')
    return render(request, 'post/post_creation.html', {'form': form})
