from django.contrib import admin

# Register your models here.

from . models import CursoEspecializacion, ProgramaLicenciatura, Licenciatura, \
    Maestria, Doctorado, PostDoctorado


admin.site.register(CursoEspecializacion)
admin.site.register(ProgramaLicenciatura)
admin.site.register(Licenciatura)
admin.site.register(Maestria)
admin.site.register(Doctorado)
admin.site.register(PostDoctorado)