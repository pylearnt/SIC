from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    help_text = 'Etiqueta para configuraciòn de URL.'


    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class Pais(models.Model):
    pais = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    codigo = models.SlugField(max_length=2, unique=True)


    def __str__(self):
        return self.pais

    class Meta:
        ordering = ['pais']
        verbose_name_plural = 'Paises'
        verbose_name = 'País'


class Estado(models.Model):
    estado = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    pais = models.ForeignKey(Pais)


    def __str__(self):
        return "{} : {}".format(self.pais, self.estado)

    class Meta:
        unique_together = ('estado', 'pais')
        ordering = ['pais', 'estado']


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    estado = models.ForeignKey(Estado)
    # pais = models.ForeignKey(Pais)  # el pais se puede calcular a partir del estado


    def __str__(self):
        return "{} : {} ".format(self.estado, self.ciudad)

    class Meta:
        unique_together = ('ciudad', 'estado')
        ordering = ['estado', 'ciudad']
        verbose_name_plural = 'Ciudades'


class Ubicacion(models.Model):
    direccion1 = models.CharField('Dirección', max_length=255)
    direccion2 = models.CharField('Dirección (continuación)', blank=True, max_length=255) #este deberia poder ser null
    slug = models.SlugField(max_length=255)
    # pais = models.ForeignKey(Pais)      # parece que estos dos campos se pueden calcular a partir de los padres de ciudad
    # estado = models.ForeignKey(Estado)  # y estado respectivapente.
    ciudad = models.ForeignKey(Ciudad)
    codigo_postal = models.IntegerField()
    telefono = models.SlugField(max_length=20)


    def __str__(self):
        return "{} : {} : {}".format(self.direccion1, self.direccion2, self.ciudad)


    class Meta:
        unique_together = ('direccion1', 'direccion2', 'ciudad')
        verbose_name_plural = 'Ubicaciones'

class Institucion(models.Model):
    institucion = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    ubicacion = models.ForeignKey(Ubicacion)


    def __str__(self):
        return self.institucion


    class Meta:
        verbose_name_plural = 'Instituciones'


class Dependencia(models.Model):
    dependencia = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    institucion = models.ForeignKey(Institucion)
    ubicacion = models.ForeignKey(Ubicacion)


    def __str__(self):
        return "{} : {}".format(self.institucion, self.dependencia)

    class Meta:
        unique_together = ('dependencia', 'institucion')



class Cargo(models.Model):
    cargo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    #institucion = models.ForeignKey(Institucion)
    dependencia = models.ForeignKey(Dependencia)

    def __str__(self):
        return "[{}] : {}".format(self.cargo, self.dependencia)

    class Meta:
        unique_together = ('cargo', 'dependencia')


class Entidad(models.Model):
    entidad = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    dependencia = models.ForeignKey(Dependencia)

    def __str__(self):
        return "[{}] : {}".format(self.entidad, self.dependencia)

    class Meta:
        unique_together = ('entidad', 'dependencia')
        verbose_name_plural = 'Entidades'


class ComisionAcademica(models.Model):
    comision_academica = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    dependencia = models.ForeignKey(Dependencia)

    def __str__(self):
        return "[{}] : {}".format(self.comision_academica, self.dependencia)

    class Meta:
        verbose_name_plural = 'Comisiones académicas'


class ComisionEvaluacion(models.Model):
    comision_evaluacion = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    dependencia = models.ForeignKey(Dependencia)

    def __str__(self):
        return "[{}] : {}".format(self.comision_evaluacion, self.dependencia)

    class Meta:
        verbose_name_plural = 'Comisiones de evaluación'


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