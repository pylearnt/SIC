from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo, Proyecto
from publicacion.models import TipoDocumento, Revista, Indice, Libro, Editorial, Coleccion
from investigacion.models import CapituloLibroInvestigacion
# Create your models here.

class ArbitrajePublicacion(models.Model):
    tipo_publicacion = models.CharField(max_length=20, choices=(('REVISTA', 'Revista'), ('LIBRO', 'Libro'), ('CAPITULO_LIBRO', 'Capitulo en libro')))
    descripcion = models.TextField(blank=True)
    indices = models.ManyToManyField(Indice, related_name='arbitraje_publicacion_indices', blank=True)
    revista = models.ForeignKey(Revista, blank=True)
    libro = models.ForeignKey(Libro, blank=True)
    capitulo_libro = models.ForeignKey(CapituloLibroInvestigacion, blank=True)
    fecha_dictamen = models.DateField()
    participantes = models.ManyToManyField(User, related_name='arbitraje_publicacion_participantes', blank=True)

    def __str__(self):
        lista_titulos = [self.revista, self.libro, self.capitulo_libro]
        titulo = [x for x in lista_titulos if x != 'n/a']
        titulo = titulo[0]
        return "{} : {}".format(self.tipo_publicacion.title(), titulo, self.fecha_dictamen)

    class Meta:
        ordering = ['-fecha_dictamen']
        verbose_name = 'Arbitraje en publicaciones académicas'
        verbose_name_plural = 'Arbitrajes en publicaciones académicas'


class ArbitrajeProyectoInvestigacion(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    proyecto = models.ForeignKey(Proyecto)
    participantes = models.ManyToManyField(User, related_name='arbitraje_proyecto_investigacion_participantes', blank=True)

    def __str__(self):
        return "{} : {}".format(str(self.proyecto), self.fecha)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Arbitraje de proyectos de investigación'
        verbose_name_plural = 'Arbitrajes de proyectos de investigación'


class ArbitrajeOtrasActividades(models.Model):
    actividad = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='actividad', unique=True)
    descripcion = models.TextField(blank=True)
    dependencia = models.ForeignKey(Dependencia)
    fecha = models.DateField()
    participantes = models.ManyToManyField(User, related_name='arbitraje_otras_actividades_participantes', blank=True)

    def __str__(self):
        return "{} : {}".format(self.actividad, self.dependencia)


