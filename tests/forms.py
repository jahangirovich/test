from django.contrib.auth.models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import PasswordInput
class MyForm(UserCreationForm):
    username = forms.CharField(label='ИИН',max_length=100)
    password1 = forms.CharField(max_length=100,label='Пароль',widget=PasswordInput())
    password2 = forms.CharField(max_length=100,label='Повторите пароль',widget=PasswordInput())
    email = forms.EmailField(max_length=100,label='Емайл')
    first_name = forms.CharField(max_length=100,label='Имя')
    class Meta:
        model = User
        fields = ('email','username','first_name','password1','password2')


class Authentication(AuthenticationForm):
    username = forms.CharField(label='ИИН',max_length=100)
    password = forms.CharField(max_length=100,label='Пароль',widget=PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')