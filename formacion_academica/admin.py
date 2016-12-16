from django.contrib import admin

# Register your models here.

from . models import TipoCurso, CursoEspecializacion, Carrera, Licenciatura, AreaConocimiento, \
    Maestria

admin.site.register(AreaConocimiento)
admin.site.register(TipoCurso)
admin.site.register(CursoEspecializacion)
admin.site.register(Carrera)
admin.site.register(Licenciatura)
admin.site.register(Maestria)