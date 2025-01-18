# alumnos/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Carrera(models.TextChoices):
    INFORMATICA = 'INFORMATICA', 'Informática'
    ADMINISTRACION = 'ADMINISTRACION', 'Administración'
    MECANICA = 'MECANICA', 'Mecánica'
    CONSTRUCCION = 'CONSTRUCCION', 'Construcción'
    ROBOTICA = 'ROBOTICA', 'Robótica'
    CONTABILIDAD = 'CONTABILIDAD', 'Contabilidad'

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    promedio_em = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_ingreso = models.DateField()
    carrera = models.CharField(max_length=100, choices=Carrera.choices)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"