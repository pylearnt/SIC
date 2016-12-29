from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Dependencia, Beca, Proyecto, FinanciamientoUNAM, FinanciamientoExterno
from vinculacion.models import RedAcademica
from formacion_academica.models import Licenciatura, Maestria, Doctorado

# Create your models here.

class AsesorEstancia(models.Model)
    asesor = models.ForeignKey(User, related_name='asesor_estancia_asesor')
    tipo = models.CharField(max_length=30, choices=(('RESIDENCIA', 'Residencia'), ('PRACTICA', 'Práctica'), ('ESTANCIA', 'Estancia'), ('SERVICIO_SOCIAL', 'Servicio Social'), ('OTRO', 'Otro')))
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    asesorado = models.ForeignKey(User, related_name='asesor_estancia_asesorado')
    nivel = models.CharField(max_length=30, choices=(('LICENCIATURA', 'licenciatura'), ('MAESTRIA', 'Maestría'), ('DOCTORADO', 'Doctorado')))
    beca = models.ForeignKey(Beca)
    proyecto = models.ForeignKey(Proyecto)
    licenciatura = models.ForeignKey(Licenciatura)
    maestria = models.ForeignKey(Maestria)
