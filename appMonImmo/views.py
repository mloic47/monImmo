from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')

def contact(request):
    return render(request, 'contact.html')

def view_property(request):
    return render(request, 'view_property.html')   

def search(request):
    return render(request, 'search.html')

def about(request):
    return render(request, 'about.html')