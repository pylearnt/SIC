from django.db import models

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Dependencia, FinanciamientoUNAM, FinanciamientoExterno
from vinculacion.models import RedAcademica
from investigacion.models import ProyectoInvestigacion

# Create your models here.


class Vinculacion(models.Model):
    tipo = models.CharField(max_length=30, choices=(('INVITACION', 'Invitación'), ('ESTANCIA', 'Estancia de colaboración'), ('SABATICO', 'Sabático')))
    academico = models.ForeignKey(User)
    descripcion = models.TextField(blank=True)
    dependencia = models.ForeignKey(Dependencia)
    actividades = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    intercambio_unam = models.BooleanField(default=False)
    financiamiento_unam = models.ForeignKey(FinanciamientoUNAM)
    convocatoria_financiamiento_unam = models.CharField(max_length=255, blank=True)
    financiamiento_externo = models.ForeignKey(FinanciamientoExterno)
    redes_academicas = models.ManyToManyField(RedAcademica, related_name='vinculacion_redes_academicas', blank=True)
    proyectos_investigacion = models.ManyToManyField(ProyectoInvestigacion, related_name='vinculacion_proyectos_investigacion', blank=True)
    tags = models.ForeignKey(Tag, related_name='vinculacion_tags')

    def __str__(self):
        return "{} : {}".format(str(self.academico), str(self.dependencia))

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Actividad de vinculación'
        verbose_name_plural = 'Actividades de vinculación'


class Invitado(models.Model):
    invitado = models.ForeignKey(User)
    descripcion = models.TextField(blank=True)
    dependencia_procedencia = models.ForeignKey(Dependencia)
    actividades = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    intercambio_unam = models.BooleanField(default=False)
    financiamiento_unam = models.ForeignKey(FinanciamientoUNAM)
    convocatoria_financiamiento_unam = models.CharField(max_length=255, blank=True)
    financiamiento_externo = models.ForeignKey(FinanciamientoExterno)
    redes_academicas = models.ManyToManyField(RedAcademica, related_name='invitado_redes_academicas', blank=True)
    proyectos_investigacion = models.ManyToManyField(ProyectoInvestigacion, related_name='invitado_proyectos_investigacion', blank=True)
    tags = models.ForeignKey(Tag, related_name='invitado_tags')

    def __str__(self):
        return "{} : {}".format(str(self.invitado), str(self.dependencia_procedencia))

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Invitado nacional'
        verbose_name_plural = 'Invitados nacionales'


class EstanciaColaboracion(models.Model):
    academico = models.ForeignKey(User)
    descripcion = models.TextField(blank=True)
    dependencia_visitada = models.ForeignKey(Dependencia)
    actividades = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    intercambio_unam = models.BooleanField(default=False)
    financiamiento_unam = models.ForeignKey(FinanciamientoUNAM)
    convocatoria_financiamiento_unam = models.CharField(max_length=255, blank=True)
    financiamiento_externo = models.ForeignKey(FinanciamientoExterno)
    redes_academicas = models.ManyToManyField(RedAcademica, related_name='estancia_colaboracion_academicas', blank=True)
    proyectos_investigacion = models.ManyToManyField(ProyectoInvestigacion, related_name='estancia_colaboracion_investigacion', blank=True)
    tags = models.ForeignKey(Tag, related_name='estancia_tags')

    def __str__(self):
        return "{} : {}".format(str(self.academico), str(self.dependencia_visitada))

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Estancia de colaboración'
        verbose_name_plural = 'Estancias de colaboración'