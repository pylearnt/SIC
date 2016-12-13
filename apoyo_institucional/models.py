from django.db import models

from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo, ComisionAcademica, ComisionEvaluacion
from django.contrib.auth.models import User

# Create your models here.

class Actividad(models.Model):
    actividad = models.CharField(max_length=255)
    slug = models.SlugField()
    descripcion = models.TextField()
    ubicacion = models.ForeignKey(Ubicacion)

    tags = models.ManyToManyField(Tag, related_name='actividad')

    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {}".format(self.actividad, self.ubicacion)

    class Meta:
        verbose_name_plural = 'Actividades'


class CargoApoyoInstitucional(models.Model):
    cargo = models.ForeignKey(Cargo)
    user = models.ForeignKey(User)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.cargo, self.cargo_inicio, self.cargo_fin)

    class Meta:
        verbose_name_plural = 'Cargos Apoyo Institucional'


class ComisionAcademicaApoyoInstitucional(models.Model):
    comision_academica = models.ForeignKey(ComisionAcademica)
    user = models.ForeignKey(User)
    comision_academica_inicio = models.DateField(auto_now=False)
    comision_academica_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.comision_academica, self.comision_academica_inicio, self.comision_academica_fin)

    class Meta:
        verbose_name_plural = 'Comisiónes Académicas de Apoyo Institucional'


class ComisionEvaluacionApoyoInstitucional(models.Model):
    comision_evaluacion = models.ForeignKey(ComisionEvaluacion)
    user = models.ForeignKey(User)
    comision_evaluacion_inicio = models.DateField(auto_now=False)
    comision_evaluacion_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.comision_evaluacion, self.comision_evaluacion_inicio, self.comision_evaluacion_fin)

    class Meta:
        verbose_name_plural = 'Comisiónes de Evaluación de Apoyo Institucional'

