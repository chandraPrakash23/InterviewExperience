from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import User
from .forms import MyUserCreationForm


def index(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    params = {'email':email,'password':password}
    return render(request,'index.html',params)

def login(request):
    # page = 'login'
    # if request.user.is_authenticated: 
    #     return redirect('index')
    # if request.method == 'POST':
    #     email = request.POST.get('email').lower()
    #     password = request.POST.get('password')

    #     try:
    #         user = User.objects.get(email=email)
    #     except:
    #         messages.error(request,'User does not Exits')

    #     user = authenticate(request,email=email,password=password)

    #     if user is not None:
    #         login(request,user)
    #         return redirect('index')
    #     else:
    #         messages.error(request,'Username or password does not matched')  
    # context={'page':page}
    return render(request,'login.html')

def register(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'An error occured during registration')
    return render(request,'register.html',{'form':form})