from rest_framework import serializers
from .models import *

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'comentario', 'producto', 'usuario')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'producto', 'comentario')