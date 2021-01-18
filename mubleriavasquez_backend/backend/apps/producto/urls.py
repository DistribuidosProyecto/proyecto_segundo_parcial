from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.producto import views

urlpatterns = [
    path('producto/', views.ProductoArreglo.as_view()),
    path('tela/', views.TelaArreglo.as_view()),
    path('imagen/', views.ImagenArreglo.as_view()),
    path('categoria/', views.CategoriaArreglo.as_view()),
    path('combinacion/', views.CombinacionArreglo.as_view()),
    path('tela/<int:pk>/', views.TelaDetallado.as_view()),
    path('producto/<int:pk>/', views.ProductoDetallado.as_view()),
    path('combinacion/<int:pk>/', views.CombinacionDetallado.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)