from django.db import models

from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo

# Create your models here.

class Actividad(models.Model):
    actividad = models.CharField(max_length=255)
    slug = models.SlugField()
    descripcion = models.TextField()
    ubicacion = models.ForeignKey(Ubicacion)

    tags = models.ManyToManyField(Tag, related_name='actividad')

    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "{} : {}".format(self.actividad, self.ubicacion)

class ComisionAcademica(models.Model):
    comision_academica = models.CharField(max_length=255)
    institucion = models.ForeignKey(Institucion)
    dependencia = models.ForeignKey(Dependencia)
    ciudad = models.ForeignKey(Ciudad)
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)