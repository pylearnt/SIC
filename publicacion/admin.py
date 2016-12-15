from django.contrib import admin

# Register your models here.

from . models import Editorial, StatusPublicacion, Libro, Revista, CapituloLibro, PrologoLibro, ResenaLibro

admin.site.register(Editorial)
admin.site.register(StatusPublicacion)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(CapituloLibro)
admin.site.register(PrologoLibro)
admin.site.register(ResenaLibro)