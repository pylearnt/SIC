from django.db import models

# Create your models here.

class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.nombre