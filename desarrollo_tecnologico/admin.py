from django.contrib import admin

# Register your models here.

from . models import TipoDesarrollo, Patente, Licencia, Libro, Editorial, StatusCapituloLibro, CapituloLibro, DesarrolloTecnologico

admin.site.register(TipoDesarrollo)
admin.site.register(Patente)
admin.site.register(Licencia)
admin.site.register(Libro)
#admin.site.register(Editorial)
admin.site.register(StatusCapituloLibro)
admin.site.register(CapituloLibro)
admin.site.register(DesarrolloTecnologico)