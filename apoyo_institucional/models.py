from django.db import models

# Create your models here.

class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField()
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=150)
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)
    fecha_creacion = models.DateField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_actividad

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField()

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_edicion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre


class Dependencia(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField()

    institucion = models.ForeignKey(Institucion)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_edicion = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('nombre', 'institucion',)

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=255)
    slug = models.SlugField()

    institucion = models.ForeignKey(Institucion)
    dependencia = models.ForeignKey(Dependencia, limit_choices_to={'institucion': int(institucion.id)})

    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_edicion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_cargo
