from django.contrib import admin

# Register your models here.

from . models import TipoDesarrollo, Patente, Licencia, DesarrolloTecnologico

admin.site.register(Patente)
admin.site.register(Licencia)
admin.site.register(DesarrolloTecnologico)