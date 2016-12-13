from django.contrib import admin

# Register your models here.
from . models import Actividad, CargoApoyoInstitucional, ComisionAcademicaApoyoInstitucional, ComisionEvaluacionApoyoInstitucional

admin.site.register(Actividad)
admin.site.register(CargoApoyoInstitucional)
admin.site.register(ComisionAcademicaApoyoInstitucional)
admin.site.register(ComisionEvaluacionApoyoInstitucional)



