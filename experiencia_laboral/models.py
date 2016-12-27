from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Cargo, Departamento
# Create your models here.


class ExperienciaLaboral(models.Model):
    user = models.ForeignKey(User)
    cargo = models.ForeignKey(Cargo)
    descripcion = models.TextField(blank=True)
    tipo_cargo = models.CharField(max_length=16, choices=(('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo')))
    es_permanente = models.BooleanField(default=False)
    departamento = models.ForeignKey(Departamento)
    inicio = models.DateField()
    fin = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='experiencia_laboral_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.user, self.departamento, self.cargo)

    class Meta:
        ordering = ['-inicio', 'departamento']
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"


class LineaInvestigacion(models.Model):
    user = models.ForeignKey(User)
    linea_investigacion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    es_permanente = models.BooleanField(default=False)
    inicio = models.DateField()
    fin = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='linea_investigacion_tags', blank=True)

    def __str__(self):
        return "{} : {}".format(self.user, self.linea_investigacion)

    class Meta:
        ordering = ['-inicio', 'linea_investigacion']
        verbose_name = "Línea de investigación"
        verbose_name_plural = "Líneas de investigación"


class CapacidadPotencialidad(models.Model):
    user = models.ForeignKey(User)
    competencia = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    es_permanente = models.BooleanField(default=False)
    inicio = models.DateField()
    fin = models.DateField()
    tags = models.ManyToManyField(Tag, related_name='capacidad_potencialidad_tags', blank=True)

    def __str__(self):
        return "{} : {}".format(self.user, self.competencia)

    class Meta:
        ordering = ['-inicio', 'competencia']
        verbose_name = "Capacidad y potencialid"
        verbose_name_plural = "Capacidades y potencialidades"