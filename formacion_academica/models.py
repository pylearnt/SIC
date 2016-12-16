from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion, Institucion, Dependencia
# Create your models here.

class Tesis(models.Model):
    titulo_tesis = models.CharField(max_length=255, unique=True)
    documento_tesis = models.FileField()
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User)
    asesores = models.ManyToManyField(User, related_name='tesis_asesores')
    agradecimientos = models.ManyToManyField(User, related_name='tesis_agradecimientos', blank=True)

    def __str__(self):
        return self.titulo_tesis
    class Meta:
        verbose_name_plural = 'Tesis'

class AreaConocimiento(models.Model):
    area_conocimiento = models.CharField('Área de conocimiento', max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='area_conocimiento', unique=True)

    def __str__(self):
        return self.area_conocimiento
    class Meta:
        ordering = ['area_conocimiento']
        verbose_name = 'Área de conocimiento'
        verbose_name_plural = 'Áreas de conocimiento'


class TipoCurso(models.Model):
    tipo = models.CharField(verbose_name='Tipo de curso', max_length=255, unique=True)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)

    def __str__(self):
        return self.tipo
    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de curso'
        verbose_name_plural = 'Tipos de cursos'

class CursoEspecializacion(models.Model):
    curso = models.CharField(max_length=255)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    usuarios = models.ManyToManyField(User, related_name='cursos_especializacion_usuarios')
    instructores = models.ManyToManyField(User, related_name='cursos_especializacion_instructores')
    agradecimientos = models.ManyToManyField(User, related_name='cursos_especializacion_agradecimientos', blank=True)
    tipo = models.ForeignKey(TipoCurso)
    inicio = models.DateField('Fecha de inicio', auto_now=False)
    fin = models.DateField('Fecha de finalización', blank=True)
    area_especializacion = models.ForeignKey(AreaConocimiento, verbose_name='Área de especialización')
    instituciones = models.ManyToManyField(Dependencia, related_name='cursos_especializacion')
    ubicacion = models.ForeignKey(Ubicacion, verbose_name='Ubicación')
    tags = models.ManyToManyField(Tag, related_name='cursos_especializacion', blank=True)
    slug = AutoSlugField(populate_from='curso', unique=True)

    def __str__(self):
        return "{} : {}".format(self.instituciones.all()[0], self.curso, self.inicio)
    class Meta:
        ordering = ['area_especializacion', 'curso', 'inicio']
        verbose_name = 'Curso de especialización'
        verbose_name_plural = 'Cursos de especialización'
        unique_together = ['area_especializacion', 'curso', 'inicio']


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
    usuario = models.ForeignKey(User)
    tesis = models.CharField(max_length=255)
    agradecimientos = models.ManyToManyField(User, related_name='licenciaturas', blank=True)
    carrera = models.ForeignKey(Carrera)
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de licenciatura', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de licenciatura', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado licenciatura', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.carrera, self.tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'carrera']


class Maestria(models.Model):
    usuario = models.ForeignKey(User)
    tesis = models.CharField(max_length=255)
    agradecimientos = models.ManyToManyField(User, related_name='maestrias', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de maestría', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de maestría', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado de maestría', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'tesis']


class Doctorado(models.Model):
    usuario = models.ForeignKey(User)
    tesis = models.CharField(max_length=255)
    agradecimientos = models.ManyToManyField(User, related_name='doctorados', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de doctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de doctorado', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado de doctorado', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'tesis']


class PostDoctorado(models.Model):
    usuario = models.ForeignKey(User)
    agradecimientos = models.ManyToManyField(User, related_name='postdoctorados', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de postdoctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de postdoctorado', auto_now=False, blank=True)

    def __str__(self):
        return "{} : {}".format(self.dependencia, self.area_conocimiento)