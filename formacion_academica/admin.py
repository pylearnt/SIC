from django.contrib import admin

# Register your models here.

from . models import Tesis, TipoCurso, CursoEspecializacion, Carrera, Licenciatura, AreaConocimiento, \
    Maestria, Doctorado, PostDoctorado

admin.site.register(Tesis)
admin.site.register(AreaConocimiento)
admin.site.register(TipoCurso)
admin.site.register(CursoEspecializacion)
admin.site.register(Carrera)
admin.site.register(Licenciatura)
admin.site.register(Maestria)
admin.site.register(Doctorado)
admin.site.register(PostDoctorado)