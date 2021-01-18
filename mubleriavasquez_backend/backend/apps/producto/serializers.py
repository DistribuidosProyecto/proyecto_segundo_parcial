from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'titulo', 'precio', 'descripcion',
                  'available','categoria')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombreCategoria')

class TelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tela
        fields = ('id', 'nombre', 'imagen', )

class CombinacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combinacion
        fields = ('id', 'precio_factor', 'producto', 'tela')

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('id', 'nombre', 'producto')
