from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag
from publicacion.models import Indice
# Create your models here.

class TipoDesarrollo(models.Model):
    tipo_desarrollo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    slug = AutoSlugField(populate_from='tipo_desarrollo', unique=True)

    def __str__(self):
        return self.tipo_desarrollo
    class Meta:
        ordering = ['tipo_desarrollo']
        verbose_name = 'Tipo de desarrollo'
        verbose_name_plural = 'Tipos de desarrollo'


class Proyecto(models.Model):
    proyecto = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='proyecto', unique=True)
    descripcion = models.TextField(blank=True)
    nombre_wos = models.CharField(max_length=255, unique=True, blank=True)
    autores = models.ManyToManyField(User, related_name='proyecto_autores')
    indices = models.ManyToManyField(Indice, related_name='proyecto_indices', blank=True)
    fecha = models.DateField(auto_now=False)


    def __str__(self):
        return "{} : {}".format(self.tipo, self.tipo)
    class Meta:
        ordering = ['fecha', 'proyecto']


class Licencia(models.Model):
    licencia = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    url = models.URLField()
    slug = AutoSlugField(populate_from='licencia', unique=True)

    def __str__(self):
        return self.licencia


class DesarrolloTecnologico(models.Model):
    nombre_desarrollo_tecnologico = models.CharField(max_length=255, unique=True)
    tipo_desarrollo_tecnologico = models.ForeignKey(TipoDesarrollo)
    proyectos = models.ManyToManyField(Proyecto, related_name='desarrollo_tecnologico_proyectos')
    descripcion = models.TextField()
    version = models.CharField(max_length=100)
    patente = models.CharField(max_length=255, blank=True)
    licencia = models.ForeignKey(Licencia)
    url = models.URLField(blank=True)
    autores = models.ManyToManyField(User, related_name='desarrollo_tecnologico_autores')
    agradecimientos = models.ManyToManyField(User, related_name='desarrollo_tecnologico_agradecimientos')
    tags = models.ManyToManyField(Tag, related_name='desarrollo_tecnologico_tags')
    fecha = models.DateField()
    slug = AutoSlugField(populate_from=nombre_desarrollo_tecnologico, unique=True)

    def __str__(self):
        return self.nombre_desarrollo_tecnologico
    class Meta:
        ordering = ['nombre_desarrollo_tecnologico']
        get_latest_by = ['fecha', 'nombre_desarrollo_tecnologico']
        verbose_name_plural = 'Desarrollos Tecnológicos'
