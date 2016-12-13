from django.contrib import admin

# Register your models here.

from . models import Tag, Pais, Estado, Ciudad, Ubicacion, Institucion, Dependencia, Usuario, Cargo, ComisionAcademica, ComisionEvaluacion

admin.site.register(Tag)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Ubicacion)
admin.site.register(Institucion)
admin.site.register(Dependencia)
admin.site.register(Usuario)
admin.site.register(Cargo)
admin.site.register(ComisionAcademica)
admin.site.register(ComisionEvaluacion)

