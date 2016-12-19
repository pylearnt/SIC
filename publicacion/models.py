from django.db import models

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from nucleo.models import Tag, Pais
# Create your models here.


class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='tipo', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.tipo
    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class Indice(models.Model):
    indice = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='indice', unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.indice
    class Meta:
        ordering = ['indice']


class Editorial(models.Model):
    editorial = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='editorial', unique=True)

    def __str__(self):
        return self.editorial
    class Meta:
        verbose_name_plural = 'Editoriales'


class StatusPublicacion(models.Model):
    status = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='status', unique=True)

    def __str__(self):
        return self.status
    class Meta:
        verbose_name = 'Status de publicacion'
        verbose_name_plural = 'Status de publicaciones'


class Libro(models.Model):
    libro = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='libro', unique=True)
    autores = models.ManyToManyField(User, related_name='libro_autores')
    editores = models.ManyToManyField(User, related_name='libro_editores')
    editorial = models.ForeignKey(Editorial)
    pais = models.ForeignKey(Pais)
    fecha = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    isbn = models.SlugField(max_length=20)
    tags = models.ManyToManyField(Tag, related_name='libro_tags')
    status = models.ForeignKey(StatusPublicacion)

    def __str__(self):
        return "{} : {} : {} : {}".format(self.libro, self.editorial, self.pais, self.isbn)
    class Meta:
        ordering = ['libro']
        get_latest_by = ['fecha', 'libro', 'editorial']


class Revista(models.Model):
    revista = models.CharField(max_length=255, unique=True)
    numero = models.CharField(max_length=50, unique=True)
    editorial = models.ForeignKey(Editorial)
    pais = models.ForeignKey(Pais)
    fecha = models.DateField(auto_now=False)
    url = models.URLField(blank=True)
    issn = models.SlugField(max_length=20)
    tags = models.ManyToManyField(Tag, related_name='revista_tags')
    status = models.ForeignKey(StatusPublicacion)
    slug = AutoSlugField(populate_from='libro', unique=True)

    def __str__(self):
        return "{} : {} : {}".format(self.revista, self.editorial, self.pais)
    class Meta:
        ordering = ['revista']
        get_latest_by = ['fecha', 'revista', 'editorial']


class CapituloLibro(models.Model):
    capitulo = models.CharField(max_length=255)
    libro = models.ForeignKey(Libro)
    autores = models.ManyToManyField(User, related_name='capitulo_libro_autores')
    agradecimientos = models.ManyToManyField(User, related_name='capitulo_libro_agradecimientos')
    fecha = models.DateField(auto_now=False)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()

    def __str__(self):
        return "{} : {}".format(self.capitulo, self.libro, )
    class Meta:
        ordering = ['libro', 'capitulo']
        get_latest_by = ['fecha', 'libro', 'capitulo']
        verbose_name = 'Capítulo de libro'
        verbose_name_plural = 'Capítulos de libros'


class PrologoLibro(models.Model):
    libro = models.ForeignKey(Libro)
    autores = models.ManyToManyField(User, related_name='prologo_libro_autores')
    agradecimientos = models.ManyToManyField(User, related_name='prologo_libro_agradecimientos')
    fecha = models.DateField(auto_now=False)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()

    def __str__(self):
        return self.libro
    class Meta:
        ordering = ['libro']
        get_latest_by = ['fecha', 'libro']
        verbose_name = 'Prólogo de libro'
        verbose_name_plural = 'Prólogos de libros'


class ResenaLibro(models.Model):
    libro = models.ForeignKey(Libro)
    autores = models.ManyToManyField(User, related_name='resena_libro_autores')
    agradecimientos = models.ManyToManyField(User, related_name='resena_libro_agradecimientos')
    fecha = models.DateField(auto_now=False)
    pagina_inicio = models.PositiveIntegerField()
    pagina_fin = models.PositiveIntegerField()

    def __str__(self):
        return self.libro
    class Meta:
        ordering = ['libro']
        get_latest_by = ['fecha', 'libro']
        verbose_name = 'Reseña de libro'
        verbose_name_plural = 'Reseñas de libros'