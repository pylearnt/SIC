from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion
# Create your models here.

class Memoria(models.Model):
    memoria = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='memoria')

    def __str__(self):
        return self.memoria

class Editor(models.Model):
    editor = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='editor')

    def __str__(self):
        return self.editor

class Indice(models.Model):
    indice = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='indice')

    def __str__(self):
        return self.indice

class ArticuloMemoriaCongreso(models.Model):
    titulo = models.CharField(max_length=255)
    descipcion = models.TextField(blank=True)
    memoria = models.ForeignKey(Memoria)
    editores = models.ManyToManyField(Editor, related_name='articulo_memoria_congreso_editores')
    autores_adscritos = models.ManyToManyField(User, related_name='articulo_memoria_congreso_autores_adscritos')
    autores_externos = models.ManyToManyField(User, related_name='articulo_memoria_congreso_autores_externos')
    indices = models.ManyToManyField(Indice, related_name='articulo_memoria_congreso_indices')
    pais = models.ForeignKey(Pais)
    fecha = models.DateField()
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    issn = models.SlugField(max_length=20)
    agradecimientos = models.ManyToManyField(User, related_name='articulo_memoria_congreso_agradecimientos', blank=True)
    ubicacion = models.ForeignKey(Ubicacion)
    vinculo = models.CharField(max_length=255, default="Este no se como se usa, estaba en las tablas")

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Artículo en extenso en memoria de congreso'
        verbose_name_plural = 'Artículos en extenso en memorias de congresos'

