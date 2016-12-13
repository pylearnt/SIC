from django.contrib import admin

# Register your models here.

from . models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Cargo, Usuario

admin.site.register(Tag)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Ubicacion)
admin.site.register(Institucion)
admin.site.register(Dependencia)
admin.site.register(Cargo)
admin.site.register(Usuario)

