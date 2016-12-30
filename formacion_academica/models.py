from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion, Institucion, Dependencia, AreaConocimiento, AreaEspecialidad, \
    ProgramaLicenciatura, ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion

CURSO_ESPECIALIZACION_TIPO = getattr(settings, 'CURSO_ESPECIALIZACION_TIPO', (('CURSO', 'Curso'), ('DIPLOMADO', 'Diplomado'), ('CERTIFICACION', 'Certificación'), ('OTRO', 'Otro')))
CURSO_ESPECIALIZACION_MODALIDAD = getattr(settings, 'CURSO_ESPECIALIZACION_MODALIDAD', (('PRESENCIAL', 'Presencial'), ('EN_LINEA', 'En línea'), ('MIXTO', 'Mixto'), ('OTRO', 'Otro')))

# Create your models here.


class CursoEspecializacion(models.Model):
    nombre_curso = models.CharField(max_length=255, verbose_name='Nombre del curso')
    slug = AutoSlugField(populate_from='nombre_curso', unique=True)
    descripcion = models.TextField(verbose_name='Descripción', blank=True)
    fecha_inicio = models.DateField('Fecha de inicio')
    fecha_fin = models.DateField('Fecha de finalización', blank=True, null=True)
    area_conocimiento = models.ForeignKey(AreaConocimiento, verbose_name='Área de conocimiento')
    #programa_especializacion = models.ForeignKey(ProgramaEspecializacion, verbose_name='Programa de especialización')
    instructores = models.ManyToManyField(User, related_name='_curso_especializacion_instructores')
    enrolados = models.ManyToManyField(User, related_name='_curso_especializacion_enrolados', blank=True)
    dependencias = models.ManyToManyField(Dependencia, related_name='_curso_especializacion_dependencias', blank=True)
    ubicacion = models.ForeignKey(Ubicacion, verbose_name='Ubicación', blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=CURSO_ESPECIALIZACION_TIPO, verbose_name='Tipo de curso')
    modalidad = models.CharField(max_length=20, choices=CURSO_ESPECIALIZACION_MODALIDAD)
    horas = models.PositiveIntegerField(verbose_name='Número de horas')
    tags = models.ManyToManyField(Tag, related_name='_curso_especializacion_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.area_conocimiento, self.nombre_curso, self.fecha_inicio)

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Curso de especialización'
        verbose_name_plural = 'Cursos de especialización'
        unique_together = ['area_conocimiento', 'nombre_curso', 'fecha_inicio']


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