from django.shortcuts import render

from .models import Project 
from interests.models import Interest

def home(request):
    projects = Project.objects
    interests = Interest.objects
    return render(request,'projects/home.html',{'projects':projects,'interests':interests})

