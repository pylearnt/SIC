from django.db import models

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Dependencia, FinanciamientoUNAM, FinanciamientoExterno
from vinculacion.models import RedAcademica
from investigacion.models import ProyectoInvestigacion
from formacion_academica.models import Licenciatura, Maestria, Doctorado

# Create your models here.

class CursoEscolarizado(models.Model):
    nivel = models.CharField(max_length=30, choices=(('LICENCIATURA', 'Licenciatura'), ('MAESTRIA', 'Maestría'), ('DOCTORADO', 'Doctorado')))
    licenciatura = models.ForeignKey(Licenciatura, blank=True, null=True)
    maestria = models.ForeignKey(Maestria, blank=True, null=True, enumerate=)

    docente = models.ForeignKey(User)

    def __str__(self):
        return "algo"
