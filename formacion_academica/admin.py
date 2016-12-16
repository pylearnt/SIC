from django.contrib import admin

# Register your models here.

from . models import AreaEspecializacion, TipoCurso, CursoEspecializacion, Carrera, Licenciatura, AreaConocimiento, \
    Maestria

admin.site.register(AreaEspecializacion)
admin.site.register(TipoCurso)
admin.site.register(CursoEspecializacion)
admin.site.register(Carrera)
admin.site.register(Licenciatura)
admin.site.register(AreaConocimiento)
admin.site.register(Maestria)