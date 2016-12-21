from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo
from publicacion.models import TipoDocumento, Revista, Indice, Libro, Editorial, Coleccion
from desarrollo_tecnologico.models import Proyecto

STATUS_PUBLICACION = getattr(settings, 'STATUS_PUBLICACION', (('PUBLICADO', 'Publicado'), ('EN_PRENSA', 'En prensa'), ('ACEPTADO', 'Aceptado'), ('ENVIADO', 'Enviado'), ('OTRO', 'Otro')))

# Create your models here.

class TipoProblemaNacional(models.Model):
    tipo_problema = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='tipo_problema', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_problema

    class Meta:
        verbose_name = 'Tipo de problema nacional'
        verbose_name_plural = 'Tipos de problemas nacionales'


class ProblemaNacional(models.Model):
    tipo_problema = models.ForeignKey(TipoProblemaNacional)
    problema = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='problema', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.problema

    class Meta:
        ordering = ['problema']
        verbose_name = 'problema nacional'
        verbose_name_plural = 'Problemas nacionales'


class ProyectoInvestigacion(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    descripcion = models.TextField(blank=True)
    problema_nacional = models.ManyToManyField(ProblemaNacional, related_name='proyecto_investigacion_problemas_nacionales')

    def __str__(self):
        return self.proyecto
    class Meta:
        verbose_name = "Proyecto de investigación"
        verbose_name_plural = "Proyectos de investigación"
        ordering = ['proyecto']


class ArticuloCientifico(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    documento_articulo = models.FileField()
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=16, choices=(('ARTICULO', 'Artículo'), ('ACTA', 'Acta'), ('CARTA', 'Carta'), ('RESENA', 'Reseña'), ('OTRO', 'Otro')))
    revista = models.ForeignKey(Revista)
    status = models.CharField(max_length=20, choices=STATUS_PUBLICACION)
    indizado = models.BooleanField(default=False)
    nombre_abreviado_wos = models.CharField(max_length=255, blank=True)
    autores = models.ManyToManyField(User, related_name='articulo_cientifico_autores')
    alumnos = models.ManyToManyField(User, related_name='articulo_cientifico_alumnos')
    indices = models.ManyToManyField(Indice, related_name='articulo_cientifico_indices', blank=True)
    solo_electronico = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=False)
    volumen = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=100, blank=True)
    issn = models.CharField(max_length=30, blank=True)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    id_doi = models.CharField(max_length=100, blank=True)
    id_wos = models.CharField(max_length=100, blank=True)
    id_isi = models.CharField(max_length=100, blank=True)
    proyectos = models.ManyToManyField(Proyecto, related_name='articulo_cientifico_proyectos', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.titulo, self.tipo.title(), self.revista)
    class Meta:
        verbose_name = "Artículo científico"
        verbose_name_plural = "Artículos científicos"
        ordering = ['fecha', 'titulo']


class LibroPublicado(models.Model):
    libro = models.ForeignKey(Libro)
    slug = AutoSlugField(populate_from='libro.nombre_libro', unique=True)
    descripcion = models.TextField(blank=True)
    nombre_wos = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_PUBLICACION)
    proyectos = models.ManyToManyField(Proyecto, related_name='libro_publicado_proyectos')

    def __str__(self):
        return self.libro
    class Meta:
        verbose_name = "Libro publicado"
        verbose_name_plural = "Libros publicados"
        ordering = ['libro']



class CapituloLibroInvestigacion(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descripcion = models.TextField(blank=True)
    autores = models.ManyToManyField(User, related_name='capitulo_libro_investigacion_autores')
    editores = models.ManyToManyField(User, related_name='capitulo_libro_investigacion_editores', blank=True)
    coordinadores = models.ManyToManyField(User, related_name='capitulo_libro_investigacion_coordinadores', blank=True)
    libro = models.ForeignKey(Libro)
    status = models.CharField(max_length=20, choices=STATUS_PUBLICACION)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    proyectos = models.ManyToManyField(Proyecto, related_name='capitulo_libro_investigacion_proyectos')

    def __str__(self):
        return "{} : {}".format(self.titulo, self.tipo)
    class Meta:
        verbose_name = "Capítulo de libro"
        verbose_name_plural = "Capítulos de libros"
        ordering = ['titulo']


class MapaArbitrado(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descripcion = models.TextField(blank=True)
    autores = models.ManyToManyField(User, related_name='mapa_arbitrado_autores')
    editores = models.ManyToManyField(User, related_name='mapa_arbitrado_editores', blank=True)
    coordinadores = models.ManyToManyField(User, related_name='mapa_arbitrado_coordinadores', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_PUBLICACION)
    ciudad = models.ForeignKey(Ciudad)
    editorial = models.ForeignKey(Editorial)
    fecha = models.DateField(auto_now=False)
    numero_edicion = models.PositiveIntegerField(default=1)
    numero_paginas = models.PositiveIntegerField(default=1)
    coleccion = models.ForeignKey(Coleccion, blank=True)
    volumen = models.CharField(max_length=255, blank=True)
    isbn = models.SlugField(max_length=30, blank=True)
    url = models.URLField(blank=True)
    proyectos = models.ManyToManyField(Proyecto, related_name='mapa_arbitrado_proyectos')

    def __str__(self):
        return "{} : {}".format(self.titulo, self.tipo)
    class Meta:
        verbose_name = "Mapa arbitrado"
        verbose_name_plural = "Mapas arbitrados"
        ordering = ['fecha', 'titulo']


class InformeTecnico(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descripcion = models.TextField(blank=True)
    autores = models.ManyToManyField(User, related_name='informe_tecnico_autores')
    dependencias = models.ManyToManyField(Dependencia, related_name='informe_tecnico_dependencias')
    fecha = models.DateField(auto_now=False)
    numero_paginas = models.PositiveIntegerField(default=1)
    url = models.URLField(blank=True)
    proyectos = models.ManyToManyField(Proyecto, related_name='informe_tecnico_proyectos')

    def __str__(self):
        return "{} : {}".format(self.tipo, self.tipo)
    class Meta:
        verbose_name = "Informe técnico de acceso público"
        verbose_name_plural = "Informes técnicos de acceso público"
        ordering = ['fecha', 'titulo']


