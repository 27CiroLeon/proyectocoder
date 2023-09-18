from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length= 30)
    Apellido = models.CharField(max_length= 30)
    Email = models.EmailField()
   
class Profesor(models.Model):
    nombre = models.CharField(max_length= 30)
    Apellido = models.CharField(max_length= 30)
    Email = models.EmailField()
    Profesion = models.CharField(max_length= 30)
    
class Curso(models.Model):
    nombre = models.CharField(max_length= 30)
    comision = models.IntegerField()
        
class Entregable(models.Model):
    nombre = models.CharField(max_length= 30)
    fechaentrega = models.DateField()
    entrega = models.BooleanField()