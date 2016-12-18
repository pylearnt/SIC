from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo
from publicacion.models import TipoDocumento, Revista, Indice
from desarrollo_tecnologico.models import Proyecto
# Create your models here.


class ArticuloCientifico(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from=titulo, unique=True)
    descripcion = models.TextField(blank=True)
    tipo = models.ForeignKey(TipoDocumento)
    revista = models.ForeignKey(Revista)
    nombre_wos = models.CharField(max_length=255, unique=True)
    indices = models.ManyToManyField(Indice, related_name='articulo_cientifico_indices')
    solo_electronico = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=False)
    volumen = models.CharField(max_length=100, blank=True)
    numero = models.PositiveIntegerField()
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    id_doi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_wos = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    id_isi = models.CharField(max_length=100, unique=True) # Es posible que ese pueda ser de tipo slug
    issn = models.CharField(max_length=50, unique=True)
    proyectos = models.ManyToManyField(Proyecto, related_name='articulo_cientifico_proyectos')


class