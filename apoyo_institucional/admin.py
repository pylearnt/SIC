from django.contrib import admin

# Register your models here.
from . models import Actividad, CargoAcademicoAdministrativo, ComisionApoyoInstitucional

admin.site.register(Actividad)
admin.site.register(CargoAcademicoAdministrativo)
admin.site.register(ComisionApoyoInstitucional)




