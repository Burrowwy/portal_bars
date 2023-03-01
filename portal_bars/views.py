from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portal/home.html',)

def deliver(request):
    projects = Project.objects.all()
    return render(request, 'portal/deliver.html', {'projects':projects})

def restaurant(request):
    projects = Project.objects.all()
    return render(request, 'portal/restaurant.html', {'projects':projects})
