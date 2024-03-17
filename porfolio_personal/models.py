from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300, blank=True)
    imagen = models.ImageField(upload_to='porfolio/images/', blank=True)
    url = models.URLField(max_length=200, blank=True)
    fecha = models.DateField(null=True, blank=True)


class redes(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)

