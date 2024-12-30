from django.db import models

from django.contrib.auth.models import User

class EspacioDeEstudio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='espacios/', blank=True, null=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    espacio = models.ForeignKey(EspacioDeEstudio, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    creada_en = models.DateTimeField(auto_now_add=True)
