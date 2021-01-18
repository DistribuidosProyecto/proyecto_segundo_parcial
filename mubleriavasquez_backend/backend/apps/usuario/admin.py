from django.contrib import admin
from .models import Usuario, Rol, Suscripcion
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario


class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre', 'apellido', 'correo', 'telefono', 'rol',)
    resource_class = UsuarioResource


class RolResource(resources.ModelResource):
    class Meta:
        model = Rol


class RolAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreRol']
    list_display = ('id','nombreRol',)
    resource_class = RolResource


class SuscripcionResource(resources.ModelResource):
    class Meta:
        model = Suscripcion


class SuscripcionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id', 'correo',)
    resource_class = SuscripcionResource


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)

