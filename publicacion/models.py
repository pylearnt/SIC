from django.db import models

from django.conf import settings
from autoslug import AutoSlugField
from nucleo.models import User, Tag, Pais, Ciudad

STATUS_PUBLICACION = getattr(settings, 'STATUS_PUBLICACION', (('PUBLICADO', 'Publicado'), ('EN_PRENSA', 'En prensa'), ('ACEPTADO', 'Aceptado'), ('ENVIADO', 'Enviado'), ('OTRO', 'Otro')))


# Create your models here.


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo
    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class Indice(models.Model):
    indice = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='indice', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.indice
    class Meta:
        ordering = ['indice']


class Memoria(models.Model):
    memoria = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='memoria')

    def __str__(self):
        return self.memoria


class Editorial(models.Model):
    editorial = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='editorial', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.editorial
    class Meta:
        ordering = ['editorial']
        verbose_name_plural = 'Editoriales'


class Coleccion(models.Model):
    coleccion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='coleccion', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.coleccion
    class Meta:
        ordering = ['coleccion']
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'


class StatusPublicacion(models.Model):
    status = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='status', unique=True)

    def __str__(self):
        return self.status
    class Meta:
        verbose_name = 'Status de publicacion'
        verbose_name_plural = 'Status de publicaciones'


class Libro(models.Model):
    nombre_libro = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='nombre_libro', unique=True)
    descripcion = models.TextField(blank=True)
    autores = models.ManyToManyField(User, related_name='libro_autores')
    editores = models.ManyToManyField(User, related_name='libro_editores', blank=True)
    coordinadores = models.ManyToManyField(User, related_name='libro_coordinadores', blank=True)
    editorial = models.ForeignKey(Editorial)
    ciudad = models.ForeignKey(Ciudad)
    fecha = models.DateField(auto_now=False)
    numero_edicion = models.PositiveIntegerField(default=1)
    numero_paginas = models.PositiveIntegerField(default=0)
    coleccion = models.ForeignKey(Coleccion, blank=True, default=1)
    volumen = models.CharField(max_length=255, blank=True)
    isbn = models.SlugField(max_length=30)
    url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='libro_tags', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_PUBLICACION)

    def __str__(self):
        return "{} : {} : {} : {}".format(self.nombre_libro, self.editorial, self.ciudad, self.isbn)
    class Meta:
        ordering = ['nombre_libro']
        get_latest_by = ['fecha', 'nombre_libro', 'editorial']


class Revista(models.Model):
    nombre_revista = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='nombre_revista', unique=True)
    descripcion = models.TextField(blank=True)
    editorial = models.ForeignKey(Editorial)
    pais = models.ForeignKey(Pais)
    url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='revista_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.nombre_revista, self.editorial, self.pais)
    class Meta:
        ordering = ['nombre_revista']
        get_latest_by = ['fecha', 'nombre_revista', 'editorial']




