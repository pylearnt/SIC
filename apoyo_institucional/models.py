from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from datetime import datetime, date, time
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo, Entidad, \
    Comision


# Create your models here.

class Actividad(models.Model):
    actividad = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.ForeignKey(Ubicacion)

    tags = models.ManyToManyField(Tag, related_name='actividad')

    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {}".format(self.actividad, self.ubicacion)

    class Meta:
        verbose_name_plural = 'Actividades de Apoyo Institucional'


class CargoAcademicoAdministrativo(models.Model):
    cargo = models.ForeignKey(Cargo)
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)

    slug = AutoSlugField(populate_from='cargo', unique_with=('cargo', 'user', 'dependencia', 'cargo_inicio'), unique=True)

    def __str__(self):
        return "[ {} : {} ] : {} : {} : {} : {}".format(self.user, self.cargo, self.dependencia.dependencia, self.dependencia.institucion, self.cargo_inicio, self.cargo_fin)

    class Meta:
        verbose_name_plural = 'Cargos Académico-Administrativos'
        unique_together = ('cargo', 'user', 'dependencia', 'cargo_inicio')


class ComisionApoyoInstitucional(models.Model):
    comision = models.ForeignKey(Comision)
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    es_academica = models.BooleanField(default=False)
    comision_inicio = models.DateField(auto_now=False)
    comision_fin = models.DateField(auto_now=False)

    slug = AutoSlugField(populate_from='comision', unique_with=('comision', 'user', 'dependencia', 'comision_inicio'), unique =True)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.comision, self.comision_inicio, self.comision_fin)

    class Meta:
        verbose_name_plural = 'Comisiones de Apoyo Institucional'
        unique_together = ('comision', 'user', 'dependencia', 'comision_inicio')


class Representante(models.Model):
    cargo = models.ForeignKey(Cargo)
    entidad = models.ForeignKey(Entidad)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.cargo, self.cargo_inicio, self.cargo_fin)

    class Meta:
        verbose_name_plural = 'Representantes Apoyo Institucional'