from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS_PROYECTO = getattr(settings, 'STATUS_PROYECTO', (('NUEVO', 'Nuevo'), ('EN_PROCESO', 'En proceso'), ('CONCLUIDO', 'Concluído'), ('OTRO', 'Otro')))
CLASIFICACION_PROYECTO = getattr(settings, 'CLASIFICACION_PROYECTO', (('BASICO', 'Básico'), ('APLICADO', 'Aplicado'), ('DESARROLLO_TECNOLOGICO', 'Desarrollo tecnológico'), ('INNOVACION', 'Innovación'), ('INVESTIGACION_FRONTERA', 'Investigación de frontera'), ('OTRO', 'Otro')))
ORGANIZACION_PROYECTO = getattr(settings, 'ORGANIZACION_PROYECTO', (('INDIVIDUAL', 'Individual'), ('COLECTIVO', 'Colectivo')))
MODALIDAD_PROYECTO = getattr(settings, 'MODALIDAD_PROYECTO', (('DISCIPLINARIO', 'Disciplinario'), ('MULTIDISCIPLINARIO', 'Multidisciplinario'), ('INTERDISCIPLINARIO', 'Interisciplinario'), ('TRANSDISCIPLINARIO', 'Transdisciplinario'), ('OTRA', 'Otra')))
FINANCIAMIENTO_UNAM = getattr(settings, 'FINANCIAMIENTO_UNAM', (('ASIGNADO', 'Presupuesto asignado a la entidad'), ('CONCURSADO', 'Presupuesto concursado por la entidad'), ('AUTOGENERADO', 'Recursos autogenerados (extraordinarios)'), ('OTRO', 'Otro')))
FINANCIAMIENTO_EXTERNO = getattr(settings, 'FINANCIAMIENTO_UNAM', (('ESTATAL', 'Gubernamental Estatal'), ('FEDERAL', 'Gubernamental Federal'), ('LUCRATIVO', 'Privado lucrativo'), ('NO_LUCRATIVO', 'Privado no lucrativo'), ('EXTRANJERO', 'Recursos del extranjero')))
CARGO__TIPO_CARGO  = getattr(settings, 'CARGO__TIPO_CARGO', (('ACADEMICO', 'Académico'), ('ADMINISTRATIVO', 'Administrativo')))
GRADO_ACADEMICO = getattr(settings, 'GRADO_ACADEMICO', (('LICENCIATURA', 'licenciatura'), ('MAESTRIA', 'Maestría'), ('DOCTORADO', 'Doctorado')))

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='tag')
    help_text = 'Etiqueta para configuraciòn de URL.'

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class Pais(models.Model):
    pais = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='pais')
    codigo = models.SlugField(max_length=2, unique=True)

    def __str__(self):
        return self.pais

    class Meta:
        ordering = ['pais']
        verbose_name_plural = 'Paises'
        verbose_name = 'País'


class Estado(models.Model):
    estado = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='estado')
    pais = models.ForeignKey(Pais)

    def __str__(self):
        return "{} : {}".format(self.pais, self.estado)

    class Meta:
        unique_together = ['estado', 'pais']
        ordering = ['pais', 'estado']


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='ciudad')
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return "{} : {} ".format(self.estado, self.ciudad)

    class Meta:
        unique_together = ['ciudad', 'estado']
        ordering = ['estado', 'ciudad']
        verbose_name_plural = 'Ciudades'


class Region(models.Model):
    region = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='region', unique=True)
    descripcion = models.TextField(blank=True)
    paises = models.ManyToManyField(Pais, related_name='region_paises', blank=True)
    estados = models.ManyToManyField(Estado, related_name='region_estados', blank=True)
    ciudades = models.ManyToManyField(Ciudad, related_name='region_ciudades', blank=True)

    def __str__(self):
        return self.region

    class Meta:
        ordering = ['region']
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'


class Ubicacion(models.Model):
    direccion1 = models.CharField('Dirección', max_length=255)
    direccion2 = models.CharField('Dirección (continuación)', blank=True, max_length=255)
    descripcion = models.TextField(blank=True)
    ciudad = models.ForeignKey(Ciudad)
    codigo_postal = models.CharField(max_length=7, blank=True)
    telefono = models.SlugField(max_length=20, blank=True)
    slug = AutoSlugField(populate_from='direccion1', unique=True)

    def __str__(self):
        return "{} : {} : {} : {} : {}".format(self.direccion1, self.direccion2, self.ciudad.ciudad, self.ciudad.estado.estado, self.ciudad.estado.pais)

    class Meta:
        ordering = ['ciudad', 'direccion1']
        unique_together = ['direccion1', 'direccion2', 'ciudad']
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'


class Institucion(models.Model):
    institucion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='institucion')
    descripcion = models.TextField(blank=True)
    ubicacion = models.ForeignKey(Ubicacion)

    def __str__(self):
        return self.institucion

    class Meta:
        ordering = ['institucion']
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class Dependencia(models.Model):
    dependencia = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='dependencia', unique=True)
    descripcion = models.TextField(blank=True)
    institucion = models.ForeignKey(Institucion)
    ubicacion = models.ForeignKey(Ubicacion)

    def __str__(self):
        return "{} : {}".format(self.institucion, self.dependencia)

    class Meta:
        unique_together = ('dependencia', 'institucion')
        ordering = ['dependencia']


class Departamento(models.Model):
    departamento = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='dependencia', unique=True)
    descripcion = models.TextField(blank=True)
    dependencia = models.ForeignKey(Dependencia)


    def __str__(self):
        return "{} : {}".format(self.dependencia, self.departamento)

    class Meta:
        unique_together = ('departamento', 'dependencia')
        ordering = ['departamento', 'dependencia']


class Programa(models.Model):
    programa = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='programa', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.programa

    class Meta:
        ordering = ['programa']


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


class AreaWOS(models.Model):
    area_wos = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='area_wos', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.area_wos

    class Meta:
        ordering = ['area_wos']
        verbose_name = 'Área General de WOS'
        verbose_name_plural = 'Áreas Generales de WOS'


class AreaEspecialidad(models.Model):
    especialidad = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='especialidad', unique=True)
    descripcion = models.TextField(blank=True)
    area_wos = models.ForeignKey(AreaWOS)

    def __str__(self):
        return self.especialidad

    class Meta:
        ordering = ['especialidad']
        verbose_name = 'Área de especialidad de WOS y otras entidades'
        verbose_name_plural = 'Áreas de especialidades de WOS y otras entidades'


class ImpactoSocial(models.Model):
    impacto_social = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='impacto_social', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.impacto_social

    class Meta:
        ordering = ['impacto_social']
        verbose_name = 'Impacto social'
        verbose_name_plural = 'Impactos sociales'


"""
class TipoCargo(models.Model):
    tipo_cargo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='tipo_cargo', unique=True)

    def __str__(self):
        return self.tipo_cargo
    class Meta:
        verbose_name = "Tipo de cargo"
        verbose_name_plural = "Tipos de cargos"
"""


class Cargo(models.Model):
    cargo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='cargo', unique=True)

    def __str__(self):
        return self.cargo

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
"""

"""
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
"""


class FinanciamientoUNAM(models.Model):
    financiamiento = models.CharField(max_length=80, choices=FINANCIAMIENTO_UNAM)
    descripcion = models.TextField(blank=True)
    programas_financiamiento = models.ManyToManyField(Programa, related_name='financiamiento_unam_programas_financiamiento', blank=True)
    dependencias_financiamiento = models.ManyToManyField(Dependencia, related_name='financiamiento_unam_dependencias_financiamiento', blank=True)
    clave_proyecto = models.CharField(max_length=255)

    def __str__(self):
        return "{} : {}".format(self.financiamiento, self.clave_proyecto)

    class Meta:
        ordering = ['financiamiento']
        verbose_name = 'Financiamiento UNAM'
        verbose_name_plural = 'Financiamientos UNAM'


class FinanciamientoExterno(models.Model):
    financiamiento = models.CharField(max_length=80, choices=FINANCIAMIENTO_EXTERNO)
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


class Beca(models.Model):
    beca = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='beca', unique=True)
    descripcion = models.TextField(blank=True)
    dependencia = models.ForeignKey(Dependencia)

    def __str__(self):
        return "{} : {}".format(self.beca, str(self.dependencia.dependencia))


class Tesis(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='titulo')
    descripcion = models.TextField(blank=True)
    grado_academico = models.CharField(max_length=20, choices=GRADO_ACADEMICO)
    documento_tesis = models.FileField()
    alumno = models.ForeignKey(User, related_name='tesis_alumno')
    dependencia = models.ForeignKey(Dependencia)
    beca = models.ForeignKey(Beca)
    reconocimiento = models.CharField(max_length=255)
    fecha_examen = models.DateField()

    def __str__(self):
        return "{} : {}".format(self.titulo, self.alumno, self.grado_academico)

    class Meta:
        ordering = ['-fecha_examen']
        verbose_name = 'Tesis'
        verbose_name_plural = 'Tesis'


class ProgramaLicenciatura(models.Model):
    programa = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='programa', unique=True)

    def __str__(self):
        return self.programa

    class Meta:
        ordering = ['programa']
        verbose_name = 'Programa de licenciatura'
        verbose_name_plural = 'Programas de licenciatura'


class ProgramaMaestria(models.Model):
    programa = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='programa', unique=True)

    def __str__(self):
        return self.programa

    class Meta:
        ordering = ['programa']
        verbose_name = 'Programa de maestria'
        verbose_name_plural = 'Programas de maestria'


class ProgramaDoctorado(models.Model):
    programa = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='programa', unique=True)

    def __str__(self):
        return self.programa

    class Meta:
        ordering = ['programa']
        verbose_name = 'Programa de doctorado'
        verbose_name_plural = 'Programas de doctorado'


class ProgramaEspecializacion(models.Model):
    programa = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='programa', unique=True)

    def __str__(self):
        return self.programa

    class Meta:
        ordering = ['programa']
        verbose_name = 'Programa de especialización'
        verbose_name_plural = 'Programas de especialización'


class TipoEvento(models.Model):
    tipo_evento = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='tipo_evento')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo_evento
    class Meta:
        verbose_name = 'Tipo de evento'
        verbose_name_plural = 'Tipos de eventos'


class Evento(models.Model):
    nombre_evento = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='nombre_evento', unique=True)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(TipoEvento)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dependencias = models.ManyToManyField(Dependencia, related_name='_evento_dependencias')
    ubicacion = models.ForeignKey(Ubicacion)

    def __str__(self):
        return "{} : {} : {}".format(self.nombre_evento, self.fecha_inicio, self.ubicacion.ciudad)

    class Meta:
        ordering = ['fecha_inicio', 'nombre_evento']
        unique_together = ['fecha_inicio', 'nombre_evento']


class Distincion(models.Model):
    nombre_distincion = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='nombre_distincion', unique=True)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=30, choices=(('PREMIO', 'Premio'), ('DISTINCION', 'Distinción'), ('RECONOCIMIENTO', 'Reconocimiento'), ('MEDALLA', 'Medalla'), ('GUGGENHEIM', 'Beca Guggenheim'), ('HONORIS_CAUSA', 'Doctorado Honoris Causa'), ('OTRO', 'Otro')))

    def __str__(self):
        return self.nombre_distincion

    class Meta:
        ordering = ['nombre_distincion']
        verbose_name = 'Distinción'
        verbose_name_plural = 'Distinciones'



class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    es_permanente = models.BooleanField(default=False)
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False, blank=True)
    responsables = models.ManyToManyField(User, related_name='proyecto_responsables')
    participantes = models.ManyToManyField(User, related_name='proyecto_participantes', blank=True)
    status = models.CharField(max_length=30, choices=STATUS_PROYECTO)
    clasificacion = models.CharField(max_length=30, choices=CLASIFICACION_PROYECTO)
    organizacion = models.CharField(max_length=30, choices=ORGANIZACION_PROYECTO)
    modalidad = models.CharField(max_length=30, choices=MODALIDAD_PROYECTO)
    region = models.ForeignKey(Region)
    tematica_genero = models.BooleanField(default=False)
    dependencias_sic = models.ManyToManyField(Dependencia, related_name='proyecto_dependencias_sic', blank=True)
    dependencias_unam = models.ManyToManyField(Dependencia, related_name='proyecto_dependencias_unam', blank=True)
    dependencias_otras = models.ManyToManyField(Dependencia, related_name='proyecto_dependencias_otras', blank=True)
    dependencias_internacionales = models.ManyToManyField(Dependencia, related_name='proyecto_dependencias_internacionales', blank=True)
    financiamientos_unam = models.ManyToManyField(FinanciamientoUNAM, blank=True)
    financiamientos_externo = models.ManyToManyField(FinanciamientoExterno, blank=True)
    metodologias = models.ManyToManyField(Metodologia, related_name='proyecto_metodologias', blank=True)
    areas_wos = models.ManyToManyField(AreaWOS, related_name='proyecto_areas_wos')
    especialidades = models.ManyToManyField(AreaEspecialidad, related_name='proyecto_especialidades')
    impactos_sociales = models.ManyToManyField(ImpactoSocial, related_name='proyecto_impactos_sociales', blank=True)
    tecnicos = models.ManyToManyField(User, related_name='proyecto_impactos_tecnicos', blank=True)
    alumnos_doctorado = models.ManyToManyField(User, related_name='proyecto_alumnos_doctorado', blank=True)
    alumnos_maestria = models.ManyToManyField(User, related_name='proyecto_alumnos_maestria', blank=True)
    alumnos_licenciatura = models.ManyToManyField(User, related_name='proyecto_alumnos_licenciatura', blank=True)

    def __str__(self):
        return "{} : {}".format(self.nombre_proyecto, self.fecha_inicio)

    class Meta:
        ordering = ['fecha_inicio', 'nombre_proyecto']

