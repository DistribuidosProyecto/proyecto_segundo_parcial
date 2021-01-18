from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.comentario import views

urlpatterns = [
    path('comentario/', views.Comentarios.as_view()),
    path('like/', views.Likes.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

