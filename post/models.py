from django.db import models


class BlogPost (models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)


class BlogImage (models.Model):
    image = models.ImageField(upload_to='post/images')
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)