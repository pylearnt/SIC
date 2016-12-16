from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Cargo, Departamento
# Create your models here.


class ExperienciaLaboral(models.Model):
    user = models.ForeignKey(User)
    cargo = models.ForeignKey(Cargo)
    descripcion = models.TextField(blank=True)
    es_definitivo = models.BooleanField(default=False)
    departamento = models.ForeignKey(Departamento)
    tags = models.ManyToManyField(Tag, related_name='experiencias_laborales', blank=True)
    inicio = models.DateField()
    fin = models.DateField()

    def __str__(self):
        return "{} : {}".format(self.user, self.cargo.cargo, self.departamento)
    class Meta:
        ordering = ['inicio', 'departamento']
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"