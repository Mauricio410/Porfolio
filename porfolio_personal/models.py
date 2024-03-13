from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='porfolio/images/')
    url = models.URLField(max_length=200, blank=True)