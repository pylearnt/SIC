from django.db import models

# Create your models here.

class Actividad_Apoyo(models.Model):
    nombre_actividad = models.CharField(max_length=255)
    descripcion_actividad = models.TextField()
    ubicacion_actividad = models.CharField(max_length=150)
    fecha_inicio = models.DateField(auto_now=False)
    fecha_fin = models.DateField(auto_now=False)
    fecha_creacion = models.DateField(auto_now_add=True, editable=False)
    fecha_edicion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre_actividad


