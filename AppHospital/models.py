from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Medico(models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=60)
    dni = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.especialidad}"

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    obra_social = models.CharField(max_length=60)
    nro_afiliado = models.IntegerField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - DNI: {self.dni}"

class Turno(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)