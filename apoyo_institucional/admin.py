from django.contrib import admin

# Register your models here.
from . models import Actividad, Dependencia, Institucion, Cargo

admin.site.register(Actividad)
admin.site.register(Dependencia)
admin.site.register(Institucion)
admin.site.register(Cargo)



