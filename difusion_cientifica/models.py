from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais, Ubicacion
# Create your models here.



class ArticuloMemoriaCongreso(models.Model):
    titulo = models.CharField(max_length=255)
    descipcion = models.TextField(blank=True)
    memoria = models.ForeignKey(Memoria)
    editores = models.ManyToManyField(User, related_name='articulo_memoria_congreso_editores')
    autores = models.ManyToManyField(User, related_name='articulo_memoria_congreso_autores_externos')
    indices = models.ManyToManyField(Indice, related_name='articulo_memoria_congreso_indices')
    pais = models.ForeignKey(Pais)
    fecha = models.DateField()
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()
    issn = models.SlugField(max_length=20)
    agradecimientos = models.ManyToManyField(User, related_name='articulo_memoria_congreso_agradecimientos', blank=True)
    ubicacion = models.ForeignKey(Ubicacion)
    vinculo = models.CharField(max_length=255, default="Este no se como se usa, estaba en las tablas")

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Artículo en extenso en memoria de congreso'
        verbose_name_plural = 'Artículos en extenso en memorias de congresos'

