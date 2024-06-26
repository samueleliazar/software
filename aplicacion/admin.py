from django.contrib import admin
from .models import Producto


# Register your models here.

class AdmProducto(admin.ModelAdmin):
    list_display=['id', 'nombre','stock', 'descripcion']

admin.site.register(Producto,AdmProducto)
