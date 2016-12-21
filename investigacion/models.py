from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo
from publicacion.models import TipoDocumento, Revista, Indice, Libro
from desarrollo_tecnologico.models import Proyecto
# Create your models here.

class ProyectoInvestigacion(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='proyecto.proyecto', unique=True)
    nombre_wos = models.CharField(max_length=255, unique=True)
    indices = models.ManyToManyField(Indice, related_name='proyecto_investigacion_indices')
    id_doi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug

    def __str__(self):
        return "{} : {}".format(self.tipo, self.tipo)
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
    status = models.CharField(max_length=20, choices=(('PUBLICADO', 'Publicado'), ('EN_PRENSA', 'En prensa'), ('ACEPTADO', 'Aceptado'), ('ENVIADO', 'Enviado'), ('OTRO', 'Otro')))
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
    id_doi = models.CharField(max_length=100, blank=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, blank=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, blank=True) # Es posible que ese pueda ser de tipo slug
    proyectos = models.ManyToManyField(Proyecto, related_name='articulo_cientifico_proyectos', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.titulo, self.tipo.title(), self.revista)
    class Meta:
        verbose_name = "Artículo científico"
        verbose_name_plural = "Artículos científicos"
        ordering = ['fecha', 'titulo']


class LibroPublicado(models.Model):
    libro = models.ForeignKey(Libro)
    slug = AutoSlugField(populate_from='libro.libro', unique=True)
    descripcion = models.TextField(blank=True)
    nombre_wos = models.CharField(max_length=255, unique=True)
    autores = models.ManyToManyField(User, related_name='libro_publicado_autores')
    indices = models.ManyToManyField(Indice, related_name='libro_publicado_indices')
    solo_electronico = models.BooleanField(default=False)
    id_doi = models.CharField(max_length=100, unique=True)  # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True)  # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True)  # Es posible que ese pueda ser de tipo slug
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
    libro = models.ForeignKey(Libro)
    nombre_wos = models.CharField(max_length=255, unique=True)
    autores = models.ManyToManyField(User, related_name='capitulo_libro_investigacion_autores')
    indices = models.ManyToManyField(Indice, related_name='capitulo_libro_investigacion_indices')
    solo_electronico = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=False)
    volumen = models.CharField(max_length=100, blank=True)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    id_doi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    proyectos_investigacion = models.ManyToManyField(ProyectoInvestigacion, related_name='capitulo_libro_investigacion_proyectos_investigacion')

    def __str__(self):
        return "{} : {}".format(self.titulo, self.tipo)
    class Meta:
        verbose_name = "Capítulo de libro"
        verbose_name_plural = "Capítulos de libros"
        ordering = ['fecha', 'titulo']


class MapaArbitrado(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(TipoDocumento)
    nombre_wos = models.CharField(max_length=255, unique=True)
    autores = models.ManyToManyField(User, related_name='mapa_arbitrado_autores')
    indices = models.ManyToManyField(Indice, related_name='mapa_arbitrado_indices')
    solo_electronico = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=False)
    id_doi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
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
    tipo = models.ForeignKey(TipoDocumento)
    nombre_wos = models.CharField(max_length=255, unique=True)
    autores = models.ManyToManyField(User, related_name='informe_tecnico_autores')
    indices = models.ManyToManyField(Indice, related_name='informe_tecnico_indices')
    solo_electronico = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=False)
    id_doi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    proyectos = models.ManyToManyField(Proyecto, related_name='informe_tecnico_proyectos')

    def __str__(self):
        return "{} : {}".format(self.tipo, self.tipo)
    class Meta:
        verbose_name = "Informe técnico de acceso público"
        verbose_name_plural = "Informed técnicod de acceso público"
        ordering = ['fecha', 'titulo']


