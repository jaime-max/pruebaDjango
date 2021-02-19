from django.db import models

# Create your models here.
class Estudiante(models.Model):

    listaGenero = (
        ('femenino','Femenino'),
        ('masculino', 'Masculino')
    )
    estudiannte_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10, unique = True, null = False)
    nombres = models.CharField(max_length = 70, null = False)
    apellidos = models.CharField(max_length = 70, null = False)
    genero = models.CharField(max_length = 30, choices = listaGenero, default = 'femenino')
    date_created = models.DateTimeField(auto_now_add = True)
    def __str__ (self):
        return self.cedula

class Materia(models.Model):

    materia_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 70, null = False)
    nota1 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    nota2 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    nota3 = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    promedio = models.DecimalField(max_digits = 10, decimal_places = 2, null = False)
    date_created = models.DateTimeField(auto_now_add = True)


