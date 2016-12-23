from django.contrib import admin

# Register your models here.

from . models import MemoriaInExtenso, PrologoLibro, Resena


admin.site.register(MemoriaInExtenso)
admin.site.register(PrologoLibro)
admin.site.register(Resena)
