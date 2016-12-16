from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion, Institucion, Dependencia
# Create your models here.


class AreaEspecializacion(models.Model):
    area_especializacion = models.CharField('Área de conocimiento', max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='area_especializacion', unique=True)

    def __str__(self):
        return self.area_especializacion
    class Meta:
        ordering = ['area_especializacion']
        verbose_name = 'Área de especialización'
        verbose_name_plural = 'Áreas de especialización'


class TipoCurso(models.Model):
    tipo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)

    def __str__(self):
        return self.tipo
    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de curso'
        verbose_name_plural = 'Tipos de cursos'

class CursoEspecializacion(models.Model):
    curso = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    instructores = models.ManyToManyField(User, related_name='cursos_especializacion')
    tipo = models.ForeignKey(TipoCurso)
    curso_inicio = models.DateField(auto_now=False)
    curso_fin = models.DateField(blank=True)
    area_especializacion = models.ForeignKey(AreaEspecializacion)
    instituciones = models.ManyToManyField(Dependencia, related_name='cursos_especializacion')
    ubicacion = models.ForeignKey(Ubicacion)
    tags = models.ManyToManyField(Tag, related_name='cursos_especializacion', blank=True)
    slug = AutoSlugField(populate_from='curso', unique=True)

    def __str__(self):

        return "{} : {}".format(self.instituciones.all()[0], self.curso, self.curso_inicio)

    class Meta:
        ordering = ['area_especializacion', 'curso', 'curso_inicio']
        verbose_name = 'Curso de especialización'
        verbose_name_plural = 'Cursos de especialización'
        unique_together = ['area_especializacion', 'curso', 'curso_inicio']


class Carrera(models.Model):
    carrera = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='carrera', unique=True)

    def __str__(self):
        return self.carrera
    class Meta:
        verbose_name = 'carrera'
        ordering = ['carrera']


class Licenciatura(models.Model):
    tesis = models.CharField(max_length=255)
    autor = models.ForeignKey(User)
    agradecimientos = models.ManyToManyField(User, related_name='licenciaturas', blank=True)
    carrera = models.ForeignKey(Carrera)
    institucion = models.ForeignKey(Institucion)
    fecha_inicio = models.DateField('Fecha de inicio de licenciatura', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de licenciatura', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.institucion, self.carrera, self.tesis)
    class Meta:
        ordering = ['fecha_grado', 'carrera']


class AreaConocimiento(models.Model):
    area_conocimiento = models.CharField('Área de conocimiento', max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='area_conocimiento', unique=True)

    def __str__(self):
        return self.area_especializacion
    class Meta:
        ordering = ['area_conocimiento']
        verbose_name = 'Área de conocimiento'
        verbose_name_plural = 'Áreas de conocimiento'


class Maestria(models.Model):
    tesis = models.CharField(max_length=255)
    autor = models.ForeignKey(User)
    agradecimientos = models.ManyToManyField(User, related_name='licenciaturas', blank=True)
    carrera = models.ForeignKey(Carrera)
    institucion = models.ForeignKey(Institucion)
    fecha_inicio = models.DateField('Fecha de inicio de licenciatura', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de licenciatura', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.institucion, self.carrera, self.tesis)
    class Meta:
        ordering = ['fecha_grado', 'carrera']


