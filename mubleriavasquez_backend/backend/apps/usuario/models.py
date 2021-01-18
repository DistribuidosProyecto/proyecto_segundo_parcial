from django.db import models

# Create your models here.
class Rol(models.Model):
    nombreRol = models.CharField(max_length=30)
    def __str__(self):
        return self.nombreRol
class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    correo = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    contrasenia = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellido


class Suscripcion(models.Model):
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return self.correo