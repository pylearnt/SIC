from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo

# Create your models here.

class TipoDesarrollo(models.Model):
    tipo_desarrollo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from=tipo_desarrollo, unique=True)

    def __str__(self):
        return self.tipo_desarrollo


class Patente(models.Model):
    patente = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from=patente, unique=True)

    def __str__(self):
        return self.patente


class Licencia(models.Model):
    licencia = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from=licencia, unique=True)

    def __str__(self):
        return self.licencia


class DesarrolloTecnologico(models.Model):
    nombre_desarrollo_tecnologico = models.CharField(max_length=255, unique=True)
    tipo_desarrollo_tecnologico = models.ForeignKey(TipoDesarrollo)
    descripcion = models.TextField()
    version = models.CharField(max_length=100)
    patente = models.ForeignKey(Patente)
    licencia = models.ForeignKey(Licencia)
    url = models.URLField(blank=True)
    autores = models.ManyToManyField(User, related_name='autor')
    agradecimientos = models.ManyToManyField(User, related_name='agradecimiento')
    tags = models.ManyToManyField(Tag, related_name='nombre_desarrollo_tecnologico')
    fecha = models.DateField()
    slug = AutoSlugField(populate_from=nombre_desarrollo_tecnologico, unique=True)


