from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Dependencia, Beca, Proyecto, FinanciamientoUNAM, FinanciamientoExterno, \
    Tesis, ProgramaLicenciatura, ProgramaMaestria, ProgramaDoctorado
from vinculacion.models import RedAcademica
#from formacion_academica.models import Licenciatura, Maestria, Doctorado

GRADO_ACADEMICO = getattr(settings, 'GRADO_ACADEMICO', (('LICENCIATURA', 'licenciatura'), ('MAESTRIA', 'Maestría'), ('DOCTORADO', 'Doctorado')))

# Create your models here.

class AsesorEstancia(models.Model):
    asesor = models.ForeignKey(User, related_name='asesor_estancia_asesor')
    tipo = models.CharField(max_length=30, choices=(('RESIDENCIA', 'Residencia'), ('PRACTICA', 'Práctica'), ('ESTANCIA', 'Estancia'), ('SERVICIO_SOCIAL', 'Servicio Social'), ('OTRO', 'Otro')))
    asesorado = models.ForeignKey(User, related_name='asesor_estancia_asesorado')
    grado_academico = models.CharField(max_length=20, choices=GRADO_ACADEMICO)
    beca = models.ForeignKey(Beca)
    proyecto = models.ForeignKey(Proyecto)
    programa_licenciatura = models.ForeignKey(ProgramaLicenciatura)
    programa_maestria = models.ForeignKey(ProgramaMaestria)
    programa_doctorado = models.ForeignKey(ProgramaDoctorado)
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return "{} : {} : {}".format(str(self.asesor), str(self.asesorado), self.fecha_inicio)

    class Meta:
        ordering = ['-fecha_inicio', '-fecha_fin']
        verbose_name = 'Asesor en residencias / prácticas / estancias / servicio social'
        verbose_name_plural = 'Asesores en residencias / prácticas / estancias / servicio social'


class DireccionTesis(models.Model):
    grado_academico = models.CharField(max_length=20, choices=GRADO_ACADEMICO)
    fecha_inicio = models.DateField()
    fecha_examen = models.DateField()
    asesorado = models.ForeignKey(User, related_name='asesor_estancia_asesorado')
    tesis = models.ForeignKey(Tesis)