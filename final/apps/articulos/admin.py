from django.contrib import admin
from .models import Categoria, Articulo

admin.site.register(Categoria)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'resumen','contenido', 'imagen')

# Register your models here.
