from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    params = {'email':email,'password':password}
    return render(request,'index.html',params)

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html',{'form':form})