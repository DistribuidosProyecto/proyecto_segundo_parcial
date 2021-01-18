from django.shortcuts import render
from rest_framework import generics
from .models import Comentario, Like
from .serializers import *

# Create your views here.
class Comentarios(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class Likes(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer