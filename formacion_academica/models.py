from django.db import models

from django.conf import settings
from autoslug import AutoSlugField
from nucleo.models import User, Tag, Dependencia, AreaWOS, ProgramaLicenciatura, ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion, Proyecto

CURSO_ESPECIALIZACION_TIPO = getattr(settings, 'CURSO_ESPECIALIZACION_TIPO', (('CURSO', 'Curso'), ('DIPLOMADO', 'Diplomado'), ('CERTIFICACION', 'Certificación'), ('OTRO', 'Otro')))
CURSO_ESPECIALIZACION_MODALIDAD = getattr(settings, 'CURSO_ESPECIALIZACION_MODALIDAD', (('PRESENCIAL', 'Presencial'), ('EN_LINEA', 'En línea'), ('MIXTO', 'Mixto'), ('OTRO', 'Otro')))

# Create your models here.


class CursoEspecializacion(models.Model):
    nombre_curso = models.CharField(max_length=255, verbose_name='Nombre del curso')
    slug = AutoSlugField(populate_from='nombre_curso', unique=True)
    descripcion = models.TextField(verbose_name='Descripción', blank=True)
    tipo = models.CharField(max_length=20, choices=CURSO_ESPECIALIZACION_TIPO, verbose_name='Tipo de curso')
    horas = models.PositiveIntegerField(verbose_name='Número de horas')
    fecha_inicio = models.DateField('Fecha de inicio')
    fecha_fin = models.DateField('Fecha de finalización', blank=True, null=True)
    modalidad = models.CharField(max_length=20, choices=CURSO_ESPECIALIZACION_MODALIDAD)
    area_conocimiento = models.ForeignKey(AreaWOS, verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    usuario = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='_curso_especializacion_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.area_conocimiento, self.nombre_curso, self.fecha_inicio)

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Curso de especialización'
        verbose_name_plural = 'Cursos de especialización'
        unique_together = ['area_conocimiento', 'nombre_curso', 'fecha_inicio']


class Licenciatura(models.Model):
    carrera = models.ForeignKey(ProgramaLicenciatura)
    area_conocimiento = models.ForeignKey(AreaWOS, related_name='licenciatura_area_conocimiento', verbose_name='Área de conocimiento')
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    dependencia = models.ForeignKey(Dependencia)
    titulo_tesis = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    tesis = models.FileField(blank=True)
    tesis_url = models.URLField(blank=True)
    fecha_inicio = models.DateField('Fecha de inicio de licenciatura')
    fecha_fin = models.DateField('Fecha de terminación de licenciatura')
    fecha_grado = models.DateField('Fecha de obtención de grado licenciatura')
    usuario = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='licenciatura_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, str(self.carrera), self.titulo_tesis)

    class Meta:
        ordering = ['fecha_grado', 'dependencia']


class Maestria(models.Model):
    programa = models.ForeignKey(ProgramaMaestria)
    area_conocimiento = models.ForeignKey(AreaWOS, related_name='maestria_area_conocimiento', verbose_name='Área de conocimiento')
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    dependencia = models.ForeignKey(Dependencia)
    titulo_tesis = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    tesis = models.FileField(blank=True)
    tesis_url = models.URLField(blank=True)
    fecha_inicio = models.DateField('Fecha de inicio de maestría')
    fecha_fin = models.DateField('Fecha de terminación de maestría')
    fecha_grado = models.DateField('Fecha de obtención de grado de maestría')
    usuario = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='maestria_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.titulo_tesis)

    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'titulo_tesis']


class Doctorado(models.Model):
    programa = models.ForeignKey(ProgramaDoctorado)
    area_conocimiento = models.ForeignKey(AreaWOS, related_name='doctorado_area_conocimiento', verbose_name='Área de conocimiento')
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    dependencia = models.ForeignKey(Dependencia)
    titulo_tesis = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='titulo_tesis', unique=True)
    tesis = models.FileField(blank=True)
    tesis_url = models.URLField(blank=True)
    fecha_inicio = models.DateField('Fecha de inicio de doctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de doctorado', auto_now=False, blank=True, null=True)
    fecha_grado = models.DateField('Fecha de obtención de grado de doctorado', auto_now=False, blank=True)
    usuario = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='doctorado_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.dependencia, self.area_conocimiento, self.titulo_tesis)

    class Meta:
        ordering = ['fecha_grado', 'dependencia', 'titulo_tesis']


class PostDoctorado(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(verbose_name='Descripición', blank=True)
    area_conocimiento = models.ForeignKey(AreaWOS, related_name='postdoctorado_area_conocimiento', verbose_name='Área de conocimiento')
    dependencia = models.ForeignKey(Dependencia)
    proyecto = models.ForeignKey(Proyecto)
    fecha_inicio = models.DateField('Fecha de inicio de postdoctorado', auto_now=False)
    fecha_fin = models.DateField('Fecha de terminación de postdoctorado', auto_now=False)
    usuario = models.ForeignKey(User, related_name='postdoctorado_usuario')
    tags = models.ManyToManyField(Tag, related_name='post_doctorado_tags', blank=True)

    def __str__(self):
        return "{} : {} : {}".format(self.investigador, self.dependencia, self.area_conocimiento)

    class Meta:
        ordering = ['fecha_fin', 'dependencia']