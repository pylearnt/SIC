from django.contrib import admin

# Register your models here.

from . models import TipoDesarrollo, Proyecto, Licencia, Editorial, StatusPublicacion, Libro, Revista, CapituloLibro, PrologoLibro, ResenaLibro, DesarrolloTecnologico

admin.site.register(TipoDesarrollo)
admin.site.register(Proyecto)
admin.site.register(Licencia)
admin.site.register(Editorial)
admin.site.register(StatusPublicacion)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(CapituloLibro)
admin.site.register(PrologoLibro)
admin.site.register(ResenaLibro)
admin.site.register(DesarrolloTecnologico)