from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.rut

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    id_profesor = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
