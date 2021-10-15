from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def layout(request):
    return render(request, 'layout.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

