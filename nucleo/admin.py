from django.contrib import admin

# Register your models here.

from . models import Tag, Pais, Estado, Ciudad, Region, Ubicacion, Institucion, Dependencia, Departamento, \
    Programa, AreaConocimiento, AreaWOS, AreaEspecialidad, ImpactoSocial, TipoCargo, Cargo

admin.site.register(Tag)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Ubicacion)
admin.site.register(Institucion)
admin.site.register(Dependencia)
admin.site.register(Departamento)
admin.site.register(Programa)
admin.site.register(AreaConocimiento)
admin.site.register(AreaWOS)
admin.site.register(AreaEspecialidad)
admin.site.register(ImpactoSocial)
admin.site.register(TipoCargo)
admin.site.register(Cargo)

