from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import UserModel


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password confirmation', 'autocomplete': 'new-password'}))

    class Meta:
        model = UserModel
        fields = ['email', 'name', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'name': forms.TextInput(attrs={'placeholder': 'Username'})
        }


class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

    def clean(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
        else:
            email = ' '
            raise forms.ValidationError('Incorrect Email')
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Incorrect Email or password')