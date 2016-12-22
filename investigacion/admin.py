from django.contrib import admin

# Register your models here.
from . models import TipoProblemaNacional, ProblemaNacional, ArticuloCientifico, LibroPublicado, CapituloLibroInvestigacion, MapaArbitrado, InformeTecnico, \
    ProyectoInvestigacion

admin.site.register(TipoProblemaNacional)
admin.site.register(ProblemaNacional)
admin.site.register(ArticuloCientifico)
admin.site.register(LibroPublicado)
admin.site.register(CapituloLibroInvestigacion)
admin.site.register(MapaArbitrado)
admin.site.register(InformeTecnico)
admin.site.register(ProyectoInvestigacion)