from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    color = models.CharField(max_length=50)                    
    tamaño = models.CharField(max_length=50)    
    perdido_encontrado = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)
    numero_de_telefono = models.CharField(max_length=25, blank=True, null=True)
    fecha_desaparecido = models.DateField(blank=True, null=True)
    fecha_encontrado = models.DateField(blank=True, null=True)
    pais =  models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)  
    barrio = models.CharField(max_length=50)  
    info_extra = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)     

