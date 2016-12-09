from django.db import models

# Create your models here.



class Institucion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    siglas = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nombre

class Dependencia(models.Model):
    nombre = models.CharField(max_length=255)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
