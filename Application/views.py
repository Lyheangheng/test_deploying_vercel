from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'base.html')

def about(request):
    		return render(request, 'about.html')

def contact(request):
    		return render(request, 'contact.html')