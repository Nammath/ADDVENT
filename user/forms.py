from django import forms
from django.contrib.auth import authenticate, login, logout
from .models import User



class UserCreate(forms.ModelForm):
    login = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('login', 'password', 'email',)


class UserLoginForm(forms.ModelForm):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('login', 'password')