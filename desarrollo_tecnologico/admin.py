from django.contrib import admin

# Register your models here.

from . models import TipoDesarrollo, Licencia, TipoFinanciamientoUNAM, FinanciamientoUNAM, TipoFinanciamientoExterno, FinanciamientoExterno, \
    Metodologia, Proyecto, DesarrolloTecnologico

admin.site.register(TipoDesarrollo)
admin.site.register(Licencia)
admin.site.register(TipoFinanciamientoUNAM)
admin.site.register(TipoFinanciamientoExterno)
admin.site.register(FinanciamientoUNAM)
admin.site.register(FinanciamientoExterno)
admin.site.register(Metodologia)
admin.site.register(Proyecto)
admin.site.register(DesarrolloTecnologico)