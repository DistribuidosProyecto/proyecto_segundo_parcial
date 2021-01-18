from django.contrib import admin
from .models import Comentario, Like
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ComentarioResource(resources.ModelResource):
    class Meta:
        model = Comentario

class ComentarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['producto', 'usuario']
    list_display = ('id','comentario', 'producto','usuario',)
    resource_class = ComentarioResource

class LikeResource(resources.ModelResource):
    class Meta:
        model = Like

class LikeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['producto', 'usuario']
    list_display = ('id','producto', 'usuario',)
    resource_class = LikeResource

admin.site.register(Comentario,ComentarioAdmin)
admin.site.register(Like,LikeAdmin)