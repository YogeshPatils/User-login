from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import CustomUserModel
from .forms import CustomUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signUpView(request):
    fm=CustomUserForm()
    if request.method=='POST' and request.FILES:
        fm=CustomUserForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User created Successfully...')
            return redirect('signin')
    return render(request,'signup.html',{'form':fm})

def signInView(request):
    fm=AuthenticationForm()
    if request.method=='POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data.get('username')
            password=fm.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in sucessfully...')
                return redirect('home')
    return render(request,'signin.html',{'form':fm})

@login_required(login_url='/signin/')
def homeView(request):
    obj=CustomUserModel.objects.get(username=request.user.username)
    return render(request,'home.html',{'user':obj})

def logOutView(request):
    logout(request)
    messages.success(request,'logged out succesfully')
    return redirect('signin')

def updatePicView(request,id):
    user=get_object_or_404(CustomUserModel,id=id)
    if request.method=='POST' and request.FILES.get('profile_picture'):
        user.profile_picture=request.FILES['profile_picture']
        user.save()
        messages.success(request,'Success....')
        return redirect('home')
    else:
        fm=CustomUserForm(instance=user)
    return render(request,'update.html',{'form':fm})






