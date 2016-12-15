from django.contrib import admin

# Register your models here.

from . models import Memoria, Editor, Indice, ArticuloMemoriaCongreso

admin.site.register(Memoria)
admin.site.register(Editor)
admin.site.register(Indice)
admin.site.register(ArticuloMemoriaCongreso)