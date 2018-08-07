from django.shortcuts import render,redirect
# Create your views here.
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_auth,logout
from django.contrib.auth.decorators import login_required

def RegistrationView(request):
    if request.POST:
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
        if not form.is_valid():
            messages.error(request,'Простите но вы ввели неправильно что-то.Или же посмотрите правильно ли повторили пароль')
    else:
        form = MyForm()
    return render(request,'index.html',{'form':form})

def Login(request):
    if request.POST:
        form = Authentication(request.POST,data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            login_auth(request,user)
            return redirect('/main')
        if not form.is_valid():
            messages.error(request,'Простите но вы ввели неправильно что-то')
    else:
        form = Authentication()
    return render(request,'login.html',{'form':form})

@login_required
def Logout(request):
    logout(request)
    return redirect('/login')
