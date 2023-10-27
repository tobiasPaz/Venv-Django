from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    fecha_de_edicion = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Item(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    fecha_de_edicion = models.DateField(auto_now=True)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre

