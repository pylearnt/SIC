from django.db import models



from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Ubicacion, Region, Dependencia, Programa, ImpactoSocial, AreaWOS, AreaEspecialidad
from publicacion.models import Indice

from django.conf import settings

STATUS_PROYECTO = getattr(settings, 'STATUS_PROYECTO', (('NUEVO', 'Nuevo'), ('EN_PROCESO', 'En proceso'), ('CONCLUIDO', 'Concluído'), ('OTRO', 'Otro')))
CLASIFICACION_PROYECTO = getattr(settings, 'CLASIFICACION_PROYECTO', (('BASICO', 'Básico'), ('APLICADO', 'Aplicado'), ('DESARROLLO_TECNOLOGICO', 'Desarrollo tecnológico'), ('INNOVACION', 'Innovación'), ('INVESTIGACION_FRONTERA', 'Investigación de frontera'), ('OTRO', 'Otro')))
ORGANIZACION_PROYECTO = getattr(settings, 'ORGANIZACION_PROYECTO', (('INDIVIDUAL', 'Individual'), ('COLECTIVO', 'Colectivo')))
MODALIDAD_PROYECTO = getattr(settings, 'MODALIDAD_PROYECTO', (('DISCIPLINARIO', 'Disciplinario'), ('MULTIDISCIPLINARIO', 'Multidisciplinario'), ('INTERDISCIPLINARIO', 'Interisciplinario'), ('TRANSDISCIPLINARIO', 'Transdisciplinario'), ('OTRA', 'Otra')))

# Create your models here.

class TipoDesarrollo(models.Model):
    tipo_desarrollo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    slug = AutoSlugField(populate_from='tipo_desarrollo', unique=True)

    def __str__(self):
        return self.tipo_desarrollo

    class Meta:
        ordering = ['tipo_desarrollo']
        verbose_name = 'Tipo de desarrollo'
        verbose_name_plural = 'Tipos de desarrollo'


class Licencia(models.Model):
    licencia = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='licencia', unique=True)
    descripcion = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.licencia

    class Meta:
        ordering = ['licencia']


class TipoParticipacionProyecto(models.Model):
    tipo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Tipo de participación en proyecto'
        verbose_name_plural = 'Tipos de participación en proyectos'

"""
class StatusProyecto(models.Model):
    status = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='status', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status de proyecto'
        verbose_name_plural = 'Status de proyectos'

class ClasificacionProyecto(models.Model):
    clasificacion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='clasificacion', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.clasificacion

    class Meta:
        verbose_name = 'Clasificación de proyecto'
        verbose_name_plural = 'Clasificación de proyectos'

class OrganizacionProyecto(models.Model):
    organizacion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='organizacion', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.organizacion

    class Meta:
        verbose_name = 'Organización de proyecto'
        verbose_name_plural = 'Organizaciones de proyectos'

class ModalidadProyecto(models.Model):
    modalidad = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='modalidad', unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.modalidad

    class Meta:
        verbose_name = 'Organización de proyecto'
        verbose_name_plural = 'Organizaciones de proyectos'
"""


class TipoFinanciamientoUNAM(models.Model):
    tipo_presupuesto = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='tipo_presupuesto', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo_presupuesto

    class Meta:
        ordering = ['tipo_presupuesto']
        verbose_name = 'Tipo de Presupuesto UNAM'
        verbose_name_plural = 'Tipos de Presupuesto UNAM'


class FinanciamientoUNAM(models.Model):
    financiamiento = models.ForeignKey(TipoFinanciamientoUNAM)
    descripcion = models.TextField(blank=True)
    programas_financiamiento = models.ForeignKey(Programa, related_name='financiamiento_unam_programas_financiamiento')
    dependencias_financiamiento = models.ForeignKey(Dependencia, related_name='financiamiento_unam_dependencias_financiamiento', blank=True)
    clave_proyecto = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return "{} : {}".format(self.financiamiento.tipo_presupuesto, self.dependencias_financiamiento.dependencia)

    class Meta:
        ordering = ['financiamiento']
        verbose_name = 'Financiamiento UNAM'
        verbose_name_plural = 'Financiamientos UNAM'


class TipoFinanciamientoExterno(models.Model):
    tipo_financiamiento = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='tipo_financiamiento', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo_financiamiento

    class Meta:
        ordering = ['tipo_financiamiento']
        verbose_name = 'Tipo de Financiamiento (externo)'
        verbose_name_plural = 'Tipos de Financiamiento (externo)'


class FinanciamientoExterno(models.Model):
    financiamiento = models.ForeignKey(TipoFinanciamientoExterno)
    descripcion = models.TextField(blank=True)
    programas_financiamiento = models.ForeignKey(Programa, related_name='financiamiento_externo_programas_financiamiento', blank=True)
    dependencias_financiamiento = models.ForeignKey(Dependencia, related_name='financiamiento_externo_dependencias_financiamiento', blank=True)
    clave_proyecto = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{} : {}".format(self.financiamiento, self.clave_proyecto)

    class Meta:
        ordering = ['financiamiento']
        verbose_name = 'Financiamiento (externo)'
        verbose_name_plural = 'Financiamientos (externos)'


class Metodologia(models.Model):
    metodologia = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='metodologia', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.metodologia

    class Meta:
        ordering = ['metodologia']


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    es_permanente = models.BooleanField(default=False)
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False, blank=True)
    responsables = models.ManyToManyField(User, related_name='proyecto_investigacion_responsables')
    participantes = models.ManyToManyField(User, related_name='proyecto_investigacion_participantes')
    status = models.CharField(max_length=30, choices=STATUS_PROYECTO)
    clasificacion = models.CharField(max_length=30, choices=CLASIFICACION_PROYECTO)
    organizacion = models.CharField(max_length=30, choices=ORGANIZACION_PROYECTO)
    modalidad = models.CharField(max_length=30, choices=MODALIDAD_PROYECTO)
    region = models.ForeignKey(Region)
    tematica_genero = models.BooleanField(default=False)
    dependencias_sic = models.ManyToManyField(Dependencia, related_name='proyecto_investigacion_dependencias_sic', blank=True)
    dependencias_unam = models.ManyToManyField(Dependencia, related_name='proyecto_investigacion_dependencias_unam', blank=True)
    dependencias_otras = models.ManyToManyField(Dependencia, related_name='proyecto_investigacion_dependencias_otras', blank=True)
    dependencias_internacionales = models.ManyToManyField(Dependencia, related_name='proyecto_investigacion_dependencias_internacionales', blank=True)
    financiamientos_unam = models.ManyToManyField(FinanciamientoUNAM, blank=True)
    financiamientos_externo = models.ManyToManyField(FinanciamientoExterno, blank=True)
    metodologias = models.ManyToManyField(Metodologia, related_name='proyecto_investigacion_metodologias')
    areas_wos = models.ManyToManyField(AreaWOS, related_name='proyecto_investigacion_areas_wos')
    especialidades = models.ManyToManyField(AreaEspecialidad, related_name='proyecto_investigacion_especialidades')
    impactos_sociales = models.ManyToManyField(ImpactoSocial, related_name='proyecto_investigacion_impactos_sociales', blank=True)
    tecnicos = models.ManyToManyField(User, related_name='proyecto_investigacion_impactos_tecnicos', blank=True)
    alumnos_doctorado = models.ManyToManyField(User, related_name='proyecto_investigacion_alumnos_doctorado', blank=True)
    alumnos_maestria = models.ManyToManyField(User, related_name='proyecto_investigacion_alumnos_maestria', blank=True)
    alumnos_licenciatura = models.ManyToManyField(User, related_name='proyecto_investigacion_alumnos_licenciatura', blank=True)

    def __str__(self):
        return "{} : {}".format(self.nombre_proyecto, self.fecha_inicio)

    class Meta:
        ordering = ['fecha_inicio', 'nombre_proyecto']


class DesarrolloTecnologico(models.Model):
    nombre_desarrollo_tecnologico = models.CharField(max_length=255, unique=True)
    tipo_desarrollo_tecnologico = models.ForeignKey(TipoDesarrollo)
    proyectos = models.ManyToManyField(Proyecto, related_name='desarrollo_tecnologico_proyectos')
    descripcion = models.TextField()
    version = models.CharField(max_length=100)
    patente = models.CharField(max_length=255, blank=True)
    licencia = models.ForeignKey(Licencia)
    url = models.URLField(blank=True)
    autores = models.ManyToManyField(User, related_name='desarrollo_tecnologico_autores')
    agradecimientos = models.ManyToManyField(User, related_name='desarrollo_tecnologico_agradecimientos')
    tags = models.ManyToManyField(Tag, related_name='desarrollo_tecnologico_tags')
    fecha = models.DateField()
    slug = AutoSlugField(populate_from=nombre_desarrollo_tecnologico, unique=True)

    def __str__(self):
        return self.nombre_desarrollo_tecnologico
    class Meta:
        ordering = ['nombre_desarrollo_tecnologico']
        get_latest_by = ['fecha', 'nombre_desarrollo_tecnologico']
        verbose_name_plural = 'Desarrollos Tecnológicos'
