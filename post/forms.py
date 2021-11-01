from django import forms
from .models import BlogPost


class PostForm (forms.ModelForm):

    name = forms.CharField(required=True)
    content = forms.CharField(required=True)

    class Meta:
        model = BlogPost
        fields = ('name', 'content')