from django.contrib import admin

# Register your models here.

from . models import TipoDesarrollo, Proyecto, Licencia,  DesarrolloTecnologico

admin.site.register(TipoDesarrollo)
admin.site.register(Proyecto)
admin.site.register(Licencia)
admin.site.register(DesarrolloTecnologico)