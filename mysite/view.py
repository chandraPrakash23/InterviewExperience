from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    params = {'fname':fname,'lname':lname}
    return render(request,'index.html',params)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')