from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Departamento, Cargo


# Create your models here.

class Comision(models.Model):
    comision = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='comision', unique=True)

    def __str__(self):
        return self.comision
    class Meta:
        verbose_name_plural = 'Comisiones'


class Actividad(models.Model):
    actividad = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='actividad', unique=True)

    def __str__(self):
        return self.actividad
    class Meta:
        verbose_name_plural = 'Actividades'


class Representacion(models.Model):
    representacion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='representacion', unique=True)

    def __str__(self):
        return self.representacion
    class Meta:
        ordering = ['representacion']
        verbose_name = 'Representación'
        verbose_name_plural = 'Representaciones'


class OrganoColegiado(models.Model):
    organo_colegiado = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='organo_colegiado', unique=True)

    def __str__(self):
        return self.organo_colegiado
    class Meta:
        verbose_name_plural = 'Organos Colegiados'


class CargoAcademicoAdministrativo(models.Model):
    cargo = models.ForeignKey(Cargo)
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)
    slug = AutoSlugField(populate_from='cargo', unique=True)

    def __str__(self):
        return "[ {} : {} ] : {} : {} : {} : {}".format(self.user, self.cargo, self.dependencia.dependencia, self.dependencia.institucion, self.cargo_inicio, self.cargo_fin)
    class Meta:
        verbose_name_plural = 'Cargos Académico-Administrativos'
        unique_together = ('cargo', 'user', 'dependencia', 'cargo_inicio')
        ordering = ['-cargo_inicio']
        get_latest_by = ['user', 'cargo']


class RepresentanteAnteOrganoColegiado(models.Model):
    representante = models.ForeignKey(User)
    representacion = models.ForeignKey(Representacion)
    ante = models.ForeignKey(Departamento)
    dependencia = models.ForeignKey(Dependencia)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "{} : {} : {} : {} : {} - {}".format(self.representante, self.representacion, self.ante, self.dependencia, self.cargo_inicio, self.cargo_fin)
    class Meta:
        verbose_name_plural = 'Representantes Ante Organos Colegiados'
        unique_together = ('representante', 'organo_colegiado', 'user', 'dependencia', 'cargo_in    icio')
        ordering = ['-cargo_inicio']


class ComisionAcademica(models.Model):
    comision_academica = models.ForeignKey(Comision)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    ubicacion = models.ForeignKey(Ubicacion)
    comision_inicio = models.DateField(auto_now=False)
    comision_fin = models.DateField(auto_now=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='comision_academica', unique=True)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.comision_academica, self.comision_inicio, self.comision_fin)
    class Meta:
        verbose_name_plural = 'Comisiones Académicas'
        unique_together = ('comision_academica', 'user', 'dependencia', 'comision_inicio')
        ordering = ['-comision_inicio']
        get_latest_by = ['user', 'comision_academica']


class ComisionEvaluacion(models.Model):
    comision_evaluacion = models.ForeignKey(Comision)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    ubicacion = models.ForeignKey(Ubicacion)
    es_academica = models.BooleanField(default=False)
    comision_inicio = models.DateField(auto_now=False)
    comision_fin = models.DateField(auto_now=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='comision_evaluacion', unique=True)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.comision_evaluacion, self.comision_inicio, self.comision_fin)
    class Meta:
        verbose_name_plural = 'Comisiones de Evaluación'
        unique_together = ('comision_evaluacion', 'user', 'dependencia', 'comision_inicio')
        ordering = ['-comision_inicio']
        get_latest_by = ['user', 'comision_evaluacion']


class ApoyoTecnico(models.Model):
    apoyo_tecnico = models.ForeignKey(Actividad)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    ubicacion = models.ForeignKey(Ubicacion)
    apoyo_inicio = models.DateField(auto_now=False)
    apoyo_fin = models.DateField(auto_now=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='apoyo_tecnico', unique=True)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.apoyo_tecnico, self.apoyo_inicio, self.apoyo_fin)
    class Meta:
        verbose_name_plural = 'Apoyos de Técnicos'
        unique_together = ('apoyo_tecnico', 'user', 'dependencia', 'apoyo_inicio')
        ordering = ['-apoyo_inicio']
        get_latest_by = ['user', 'apoyo_tecnico']

class ApoyoOtraActividad(models.Model):
    apoyo_actividad = models.ForeignKey(Actividad)
    descripcion = models.TextField()
    user = models.ForeignKey(User)
    dependencia = models.ForeignKey(Dependencia)
    ubicacion = models.ForeignKey(Ubicacion)
    apoyo_inicio = models.DateField(auto_now=False)
    apoyo_fin = models.DateField(auto_now=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='apoyo_actividad', unique=True)

    def __str__(self):
        return "[{}] : {} : {} : {}".format(self.user, self.apoyo_actividad, self.apoyo_inicio, self.apoyo_fin)
    class Meta:
        verbose_name_plural = 'Apoyos en Otras Actividades'
        unique_together = ('apoyo_actividad', 'user', 'dependencia', 'apoyo_inicio')
        ordering = ['-apoyo_inicio']
        get_latest_by = ['user', 'apoyo_actividad']
