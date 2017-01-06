from django.contrib import admin

# Register your models here.

from . models import Tag, ZonaPais, Pais, Estado, Ciudad, Region, Ubicacion, Institucion, Dependencia, Departamento, \
    User, Programa, AreaConocimiento, AreaWOS, AreaEspecialidad, ImpactoSocial, Cargo, \
    FinanciamientoUNAM, FinanciamientoExterno, Metodologia, Beca, Tesis, ProgramaLicenciatura, \
    ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion, TipoEvento, Evento, Proyecto, Nombramiento

admin.site.register(Tag)
admin.site.register(ZonaPais)
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Region)
admin.site.register(Ubicacion)
admin.site.register(Institucion)
admin.site.register(Dependencia)
admin.site.register(Departamento)
admin.site.register(User)
admin.site.register(Programa)
admin.site.register(AreaConocimiento)
admin.site.register(AreaWOS)
admin.site.register(AreaEspecialidad)
admin.site.register(ImpactoSocial)
admin.site.register(Cargo)
admin.site.register(FinanciamientoUNAM)
admin.site.register(FinanciamientoExterno)
admin.site.register(Metodologia)
admin.site.register(Beca)
admin.site.register(Tesis)
admin.site.register(ProgramaLicenciatura)
admin.site.register(ProgramaMaestria)
admin.site.register(ProgramaDoctorado)
admin.site.register(ProgramaEspecializacion)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(Proyecto)
admin.site.register(Nombramiento)