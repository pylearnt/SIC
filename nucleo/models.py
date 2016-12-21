from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

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
        return "{} : {} ".format(self.estado, self.ciudad)

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


class TipoCargo(models.Model):
    tipo_cargo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='tipo_cargo', unique=True)

    def __str__(self):
        return self.tipo_cargo
    class Meta:
        verbose_name = "Tipo de cargo"
        verbose_name_plural = "Tipos de cargos"


class Cargo(models.Model):
    cargo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)
    tipo_cargo = models.ForeignKey(TipoCargo)
    slug = AutoSlugField(populate_from='cargo', unique=True)

    def __str__(self):
        return self.cargo






















"""
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion)
    cargo = models.ForeignKey(Cargo)
    cargo_inicio = models.DateField(auto_now=False)
    cargo_fin = models.DateField(auto_now=False)

    def __str__(self):
        return "{} : {} {} {}".format(self.user, self.nombre, self.nombre, self.apellido_paterno, self.apellido_materno)
"""