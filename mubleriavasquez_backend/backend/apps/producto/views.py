from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class CategoriaArreglo(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoArreglo(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetallado(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TelaArreglo(generics.ListCreateAPIView):
    queryset = Tela.objects.all()
    serializer_class = TelaSerializer


class TelaDetallado(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tela.objects.all()
    serializer_class = TelaSerializer

class CombinacionArreglo(generics.ListCreateAPIView):
    queryset = Tela.objects.all()
    serializer_class = TelaSerializer


class CombinacionDetallado(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combinacion.objects.all()
    serializer_class = CombinacionSerializer

class ImagenArreglo(generics.ListCreateAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer




