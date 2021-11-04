from django import forms
from django.core.validators import FileExtensionValidator


class PostForm (forms.Form):
    name = forms.CharField()
    content = forms.CharField()
    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}),
                              required=False)



