from django.contrib import admin

# Register your models here.

from . models import TipoDocumento, Indice, Editorial, StatusPublicacion, Coleccion, Libro, Revista

admin.site.register(TipoDocumento)
admin.site.register(Indice)
admin.site.register(Editorial)
admin.site.register(StatusPublicacion)
admin.site.register(Coleccion)
admin.site.register(Libro)
admin.site.register(Revista)
