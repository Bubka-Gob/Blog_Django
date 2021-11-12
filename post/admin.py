from django.contrib import admin
from .models import BlogPost, BlogImage, BlogVideo, BlogAudio, Comment

admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(BlogVideo)
admin.site.register(BlogAudio)
admin.site.register(Comment)