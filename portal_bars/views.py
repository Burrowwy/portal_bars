from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.db import IntegrityError



def registration(request):
    profile = Profile.objects.all()
    if request.method == "POST":
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=login, email=email, password=password)
        user.save()
        return redirect('home')
    return render(request, 'portal/registration.html',{"profile": profile})

def home(request):
    return render(request, 'portal/home.html',)

def deliver(request):
    projects = Project.objects.all()
    return render(request, 'portal/deliver.html', {'projects':projects})

def restaurant(request):
    projects = Project.objects.all()
    return render(request, 'portal/restaurant.html', {'projects':projects})


def authorization(request):
    projects = Project.objects.all()
    return render(request, 'portal/authorization.html', {'projects':projects})
