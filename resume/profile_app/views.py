from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')

