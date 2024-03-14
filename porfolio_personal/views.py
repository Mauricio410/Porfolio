from django.shortcuts import render
from .models import Proyectos, redes

# Create your views here.

def home(request):
    proyecto = Proyectos.objects.all()
    return render(request, 'home.html', {'proyecto':proyecto})

def proyectos(request):
    proyecto = Proyectos.objects.all()
    return render(request, 'proyectos.html', {'proyecto':proyecto})

def blog(request):
    return render(request, 'blog.html')

def sobre_mi(request):
    return render(request, 'sobre_mi.html')

def contacto(request):
    return render(request, 'contacto.html')

def redes(request):
    red = redes.objects.all()
    return render(request, 'redes.html', {'red':red})