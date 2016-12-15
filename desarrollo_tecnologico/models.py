from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo

# Create your models here.

class TipoDesarrollo(models.Model):
    tipo_desarrollo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='tipo_desarrollo', unique=True)

    def __str__(self):
        return self.tipo_desarrollo


class Patente(models.Model):
    patente = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='patente', unique=True)

    def __str__(self):
        return self.patente


class Licencia(models.Model):
    licencia = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='licencia', unique=True)

    def __str__(self):
        return self.licencia


class Libro(models.Model):
    libro = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='libro', unique=True)

    def __str__(self):
        return self.libro


class Editorial(models.Model):
    editorial = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='editorial', unique=True)

    def __str__(self):
        return self.editorial


class StatusCapituloLibro(models.Model):
    status = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='status', unique=True)

    def __str__(self):
        return self.status


class CapituloLibro(models.Model):
    capitulo = models.CharField(max_length=255)
    libro = models.ForeignKey(Libro)
    autores = models.ManyToManyField(User, related_name='capitulo_libro_autores')
    editorial = models.ForeignKey(Editorial)
    pais = models.ForeignKey(Pais)
    fecha = models.DateField(auto_now=False)
    pagina_inicio = models.PositiveIntegerField()
    paginas_fin = models.PositiveIntegerField()
    agradecimientos = models.ManyToManyField(User, related_name='capitulo_libro_agradecimientos')
    tags = models.ManyToManyField(Tag, related_name='capitulo_libro_tags')
    isbn = models.SlugField(max_length=17)
    status = models.ForeignKey(StatusCapituloLibro) # este campo muy seguramente debería cambiarse a un choices o a una clase
    url = models.URLField(blank=True)

    def __str__(self):
        return "{} : {} : {} : {}".format(self.libro, self.capitulo, self.isbn, self.pais)
    class Meta:
        ordering = ['libro', 'capitulo']
        get_latest_by = ['fecha', 'libro', 'capitulo']
        verbose_name_plural = 'Capítulos de Libros'


class DesarrolloTecnologico(models.Model):
    nombre_desarrollo_tecnologico = models.CharField(max_length=255, unique=True)
    tipo_desarrollo_tecnologico = models.ForeignKey(TipoDesarrollo)
    descripcion = models.TextField()
    version = models.CharField(max_length=100)
    patente = models.ForeignKey(Patente)
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


