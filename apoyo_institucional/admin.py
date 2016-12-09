from django.contrib import admin

# Register your models here.
from . models import Institucion, Dependencia

admin.site.register(Institucion)
admin.site.register(Dependencia)