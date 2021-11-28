from django.shortcuts import render, redirect
from .forms import PostForm
from .models import BlogPost, BlogImage, BlogVideo, BlogAudio


def post_creation_view(request):
    if not request.user.is_authenticated:
        return redirect('home-page')
    if not request.user.is_admin:
        return redirect('home-page')
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
            for video in form.files.getlist('videos'):
                video_post = BlogVideo(video=video, blog_post=blog_post)
                video_post.save()
            for audio in form.files.getlist('audio'):
                audio_post = BlogAudio(audio=audio, blog_post=blog_post)
                audio_post.save()
            return redirect('home-page')
    return render(request, 'post/post_creation.html', {'form': form})


def post_full_view(request, blog_post_id):
    # TODO content grid
    blog_post = BlogPost.objects.get(pk=blog_post_id)
    images = BlogImage.objects.filter(blog_post=blog_post_id)
    videos = BlogVideo.objects.filter(blog_post=blog_post_id)
    audios = BlogAudio.objects.filter(blog_post=blog_post_id)
    return render(request, 'post/post_full.html', {'post': blog_post,
                                                   'images': images,
                                                   'videos': videos,
                                                   'audios': audios})