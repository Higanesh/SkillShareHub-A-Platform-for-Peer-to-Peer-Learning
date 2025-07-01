from django.shortcuts import render,redirect,HttpResponse
from core.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    print(">>> register view called")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            print("exist")
            messages.add_message(request, messages.ERROR, "Username already Exists !!!")
            return render(request,'auth.html')
        
        user = User(username=username)     
        user.set_password(password)
        user.save()
        print("success")
        messages.add_message(request, messages.SUCCESS, "Registration Successfull !!!!")
        return render(request,'auth.html')
    return render(request,"auth.html")

def auth(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "invalid credentials!!!")
            return render(request,"auth.html")
        
        user = authenticate(username=username,password=password)

        if user == None:
            messages.add_message(request, messages.ERROR, "invalid credentials!!!")
            return render(request,"auth.html")
        else:
            login(request,user)
            return redirect('home')
    return render(request,"auth.html")

