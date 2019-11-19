from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/Viahire.html', {'title': 'Home'})

def about(request):
    return render(request, 'home/ViahireAbout.html', {'title': 'About'})
