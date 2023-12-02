from django.db import models

# Create your models here.
class Item(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        texto="{0} ({1})"
        return texto.format(self.nombre, self.precio)

class Objeto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.PositiveSmallIntegerField()
    info = models.CharField(max_length=70)
    
    def __str__(self) -> str:
        texto="{0} ({1})"
        return texto.format(self.nombre, self.precio)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    contra = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    
    def __str__(self) -> str:
        texto="{0} ({1})"
        return texto.format(self.nombre, self.email)