from django.contrib import admin
from .models import Producto, Categoria, Tela, Combinacion, Imagen
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreCategoria']
    list_display = ('id','nombreCategoria',)
    resource_class = CategoriaResource


class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto


class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('id','titulo', 'precio', 'descripcion', 'available', 'categoria',)
    resource_class = ProductoResource


class CombinacionResource(resources.ModelResource):
    class Meta:
        model = Combinacion


class CombinacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['precio_factor']
    list_display = ('id','precio_factor', 'producto','tela',)
    resource_class = CombinacionResource


class TelaResource(resources.ModelResource):
    class Meta:
        model = Tela


class TelaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre', 'imagen',)
    resource_class = TelaResource


class ImagenResource(resources.ModelResource):
    class Meta:
        model = Imagen


class ImagenAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre', 'producto',)
    resource_class = ImagenResource


# Register your models here.
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tela,TelaAdmin)
admin.site.register(Combinacion,CombinacionAdmin)
admin.site.register(Imagen,ImagenAdmin)
