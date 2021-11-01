from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import UserModel


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    name = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ['email', 'name', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Неверный Email или пароль')