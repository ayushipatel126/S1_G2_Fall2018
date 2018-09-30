from django.shortcuts import render

def contact(request):
    return render(request, 'home/contactUs.html')

def home(request):
    return render(request, 'home/home.html')

def signin(request):
    return render(request, 'home/signin.html')

def searchProperty(request):
    return render(request, 'home/searchProperty.html')