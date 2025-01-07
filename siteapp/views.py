from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def education(request):
    return render(request, 'education.html')

def projects(request):
    return render(request, 'projects.html')

def careerblog(request):
    return render(request, 'career-blog.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def sutoAppi(request):
    return render(request, 'suto-appi.html')