from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
def index(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    params = {'email':email,'password':password}
    return render(request,'index.html',params)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.get_user():
          user = form.save()
          login(request,user)  
          return redirect('index')
    else:
        initial_data = {'email':'','password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request,user)  
          return redirect('index')
    else:
        initial_data = {'name':'','email':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})