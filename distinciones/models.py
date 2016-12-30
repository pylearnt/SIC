from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Dependencia, Distincion

EVENTO__AMBITO = getattr(settings, 'EVENTO__AMBITO', (('INSTITUCIONAL', 'Institucional'), ('REGIONAL', 'Regional'), ('NACIONAL', 'Nacional'), ('INTERNACIONAL', 'Internacional'), ('OTRO', 'Otro')))

# Create your models here.

class DistincionObtenida(models.Model):
    fecha = models.DateField()
    distincion = models.ForeignKey(Distincion)
    descripcion = models.TextField(blank=True)
    condecorados = models.ManyToManyField(User, related_name='_condecorados')
    otorga = models.ForeignKey(Dependencia)
    ambito = models.CharField(max_length=20, choices=EVENTO__AMBITO)

    def __str__(self):
        return "{} : {}".format(self.distincion, self.fecha)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Distinción recibida'
        verbose_name_plural = 'Distinciones recibidas'