from django.shortcuts import render
from django.http import HttpResponse

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