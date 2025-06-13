from django.db import models

# Create your models here.

class Cliente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255, default="Sin dirección")


    def __str__(self):
        return f"{self.nombres} {self.apellidos}"