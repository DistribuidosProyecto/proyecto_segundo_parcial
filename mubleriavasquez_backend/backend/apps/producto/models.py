from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=30)
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    titulo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=200)
    available = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Tela(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Combinacion(models.Model):
    precio_factor = models.DecimalField(decimal_places=2, max_digits=10)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tela = models.ForeignKey(Tela,on_delete=models.CASCADE)
    def __str__(self):
        return self.precio_factor

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre