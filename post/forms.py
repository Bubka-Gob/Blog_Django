from django import forms
from django.core.validators import FileExtensionValidator


class PostForm (forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name_input'}))
    content = forms.CharField(widget=forms.Textarea())
    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}),
                              required=False)
    videos = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'accept': '.mp4,.webm'}),
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm'])],
                             required=False)
    audios = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'accept': '.mp3,.wav'}),
                             validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])],
                             required=False)



