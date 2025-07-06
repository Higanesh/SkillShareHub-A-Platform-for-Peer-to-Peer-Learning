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

def userlogout(request):
    logout(request)    
    return redirect("auth")

def create_profile(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get("profile_picture")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        bio = request.POST.get("bio")
        skills = request.POST.get("skills")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        rating = request.POST.get("rating")

        profile, created = Profile.objects.get_or_create(user=request.user)

        if profile_picture:
            profile.profile_picture = profile_picture
        profile.first_name = first_name
        profile.last_name = last_name
        profile.gender = gender
        profile.bio = bio
        profile.skills = skills
        profile.city = city
        profile.state = state
        profile.country = country
        profile.rating = rating
        profile.save()

        messages.success(request, "✅ Profile saved successfully!")
        return redirect("home")

    else:
        # Pre-fill form with existing data
        profile = Profile.objects.filter(user=request.user).first()
        return render(request, "create_profile.html", {"profile": profile})


# def update_profile(request):
#     get_profile_for_update = Profile.objects.get(request.user)
#     return render(request,"home.html",{"update_profile":get_profile_for_update})

def view_profile(request):
    view_user_profile = Profile.objects.get(user=request.user)
    return render(request,"profile.html",{"view_profile":view_user_profile})

def public_profile(request):
    profile = Profile.objects.all()
    return render(request,"public_profile.html",{"profiles":profile})

