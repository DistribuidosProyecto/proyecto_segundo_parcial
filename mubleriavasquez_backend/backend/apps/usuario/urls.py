from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.usuario import views

urlpatterns = [
    path('usuario/', views.UsuarioArreglo.as_view()),
    path('rol/', views.RolArreglo.as_view()),
    path('suscripcion/', views.SuscripcionArreglo.as_view()),
    path('usuario/<int:pk>', views.UsuarioDetallado.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)