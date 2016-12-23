from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ciudad, Ubicacion, Proyecto, TipoEvento, Evento
from publicacion.models import Libro, Revista, Indice
# Create your models here.


class MemoriaInExtenso(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)
    descipcion = models.TextField(blank=True)
    ciudad = models.ForeignKey(Ciudad)
    fecha = models.DateField()
    evento = models.ForeignKey(Evento)
    autores = models.ManyToManyField(User, related_name='_memoria_in_extenso_autores_externos')
    editores = models.ManyToManyField(User, related_name='_memoria_in_extenso_editores', blank=True)
    indices = models.ManyToManyField(Indice, related_name='_memoria_in_extenso_indices', blank=True)
    agradecimientos = models.ManyToManyField(User, related_name='_memoria_in_extenso_agradecimientos', blank=True)
    pais_origen = models.ForeignKey(Pais)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    issn = models.SlugField(max_length=20)
    proyectos = models.ForeignKey(Proyecto)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Memoria in extenso'
        verbose_name_plural = 'Memorias in extenso'


class PrologoLibro(models.Model):
    descipcion = models.TextField(blank=True)
    autor_prologo = models.ForeignKey(User)
    autores = models.ManyToManyField(User, related_name='_prologo_libro_autores', blank=True)
    editores = models.ManyToManyField(User, related_name='_prologo_libro_editores', blank=True)
    coordinadores = models.ManyToManyField(User, related_name='_prologo_libro_coordinadores', blank=True)
    libro = models.ForeignKey(Libro, related_name='_prologo_libro_libro')
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    url = models.URLField(blank=True)

    def __str__(self):
        return '{} : {}'.format(self.autor_prologo, self.libro)

    class Meta:
        verbose_name = 'Prólogo de libro'
        verbose_name_plural = 'Prólogos de libros'


class Resena(models.Model):
    titulo_resena = models.CharField(max_length=255, unique=True)
    tipo_publicacion = models.CharField(max_length=20, choices=(('LIBRO', 'Libro'), ('REVISTA', 'Revista'), ('OTRO', 'Otro')))
    libro = models.ForeignKey(Libro, null=True, related_name='_resena_libro')
    revista = models.ForeignKey(Revista, related_name='_resena_revista', null=True)
    volumen = models.CharField(max_length=10, blank=True)
    slug = AutoSlugField(populate_from='titulo_resena', unique=True)
    descipcion = models.TextField(blank=True)
    revistas = models.ManyToManyField(Revista, related_name='_resena_revistas', blank=True)
    libros = models.ManyToManyField(Libro, related_name='_resena_libros', blank=True)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()

    autor_resena = models.ForeignKey(User)
    autores = models.ManyToManyField(User, related_name='_resena_autores', blank=True)
    editores = models.ManyToManyField(User, related_name='_resena_editores', blank=True)
    coordinadores = models.ManyToManyField(User, related_name='_resena_coordinadores', blank=True)


    url = models.URLField(blank=True)

    def __str__(self):
        return '{} : {}'.format(self.autor_resena, self.titulo_resena)

    class Meta:
        verbose_name = 'Reseña de libro'
        verbose_name_plural = 'Reseñas de libros'


class OrganizacionEventoAcademico(models.Model):
    nombre_evento = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='nombre_evento', unique=True)
    tipo = models.ForeignKey(TipoEvento)

    def __str__(self):
        return self.nombre_evento