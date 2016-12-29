from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion, Institucion, Dependencia, AreaConocimiento, AreaEspecialidad, \
    ProgramaLicenciatura, ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion

CURSO_ESPECIALIZACION_TIPO = getattr(settings, 'CURSO_ESPECIALIZACION_TIPO', (('CURSO', 'Curso'), ('DIPLOMADO', 'Diplomado'), ('CERTIFICACION', 'Certificación'), ('OTRO', 'Otro')))
CURSO_ESPECIALIZACION_MODALIDAD = getattr(settings, 'CURSO_ESPECIALIZACION_MODALIDAD', (('PRESENCIAL', 'Presencial'), ('EN_LINEA', 'En línea'), ('MIXTO', 'Mixto'), ('OTRO', 'Otro')))

# Create your models here.

"""
class TipoCurso(models.Model):
    tipo = models.CharField(verbose_name='Tipo de curso', max_length=255, unique=True)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de curso'
        verbose_name_plural = 'Tipos de curso (no usado ya)'
"""

class CursoEspecializacion(models.Model):
    curso = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='curso', unique=True)
    programa = models.ForeignKey(ProgramaEspecializacion)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    instructores = models.ManyToManyField(User, related_name='cursos_especializacion_instructores')
    enrolados = models.ManyToManyField(User, related_name='cursos_especializacion_enrolados')
    agradecimientos = models.ManyToManyField(User, related_name='cursos_especializacion_agradecimientos', blank=True)
    tipo = models.CharField(max_length=16, choices=CURSO_ESPECIALIZACION_TIPO)
    modalidad = models.CharField(max_length=16, choices=CURSO_ESPECIALIZACION_MODALIDAD)
    inicio = models.DateField('Fecha de inicio', auto_now=False)
    fin = models.DateField('Fecha de finalización', blank=True)
    horas = models.PositiveIntegerField()
    area_conocimiento = models.ForeignKey(AreaConocimiento, verbose_name='Área de conocimiento')
    dependencias = models.ManyToManyField(Dependencia, related_name='cursos_especializacion')
    ubicacion = models.ForeignKey(Ubicacion, verbose_name='Ubicación')
    tags = models.ManyToManyField(Tag, related_name='curso_especializacion_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.area_conocimiento, self.curso, self.inicio)
    class Meta:
        ordering = ['area_conocimiento', 'curso', 'inicio']
        verbose_name = 'Curso de especialización'
        verbose_name_plural = 'Cursos de especialización'
        unique_together = ['area_conocimiento', 'curso', 'inicio']


class Licenciatura(models.Model):
    titulo_tesis = models.CharField(max_length=255)
    programa = models.ForeignKey(ProgramaLicenciatura)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    tesis = models.FileField()
    asesor = models.ForeignKey(User, related_name='licenciatura_asesor')
    alumno = models.ForeignKey(User, related_name='licenciatura_alumno')
    agradecimientos = models.ManyToManyField(User, related_name='licenciatura_agradecimientos', blank=True)
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de licenciatura', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de licenciatura', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado licenciatura', auto_now=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name='licenciatura_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, str(self.programa), self.titulo_tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia']


class Maestria(models.Model):
    titulo_tesis = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    programa = models.ForeignKey(ProgramaMaestria)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    tesis = models.FileField()
    asesor = models.ForeignKey(User, related_name='maestria_asesor')
    alumno = models.ForeignKey(User, related_name='maestria_alumno')
    agradecimientos = models.ManyToManyField(User, related_name='maestria_agradecimientos', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, related_name='maestria_area_conocimiento', verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de maestría', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de maestría', auto_now=False, blank=True)
    fecha_grado = models.DateField('Fecha de obtención de grado de maestría', auto_now=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name='maestria_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.titulo_tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'titulo_tesis']


class Doctorado(models.Model):
    titulo_tesis = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    programa = models.ForeignKey(ProgramaDoctorado)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    tesis = models.FileField()
    asesor = models.ForeignKey(User, related_name='doctorado_asesor')
    alumno = models.ForeignKey(User, related_name='doctorado_alumno')
    agradecimientos = models.ManyToManyField(User, related_name='doctorado_agradecimientos', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, related_name='doctorado_area_conocimiento', verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de doctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de doctorado', auto_now=False, blank=True, null=True)
    fecha_grado = models.DateField('Fecha de obtención de grado de doctorado', auto_now=False, blank=True)
    tags = models.ManyToManyField(Tag, related_name='doctorado_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.titulo_tesis)
    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'titulo_tesis']


class PostDoctorado(models.Model):
    investigador = models.ForeignKey(User, related_name='postdoctorado_investigador')
    agradecimientos = models.ManyToManyField(User, related_name='postdoctorado_agradecimientos', blank=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, related_name='postdoctorado_area_conocimiento', verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    fecha_inicio = models.DateField('Fecha de inicio de postdoctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de postdoctorado', auto_now=False)
    tags = models.ManyToManyField(Tag, related_name='post_doctorado_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.investigador, self.dependencia, self.area_conocimiento)