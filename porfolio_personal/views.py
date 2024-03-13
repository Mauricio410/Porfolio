from django.shortcuts import render
from .models import Proyectos

# Create your views here.

def home(request):
    proyecto = Proyectos.objects.all()
    return render(request, 'home.html', {'proyecto':proyecto})