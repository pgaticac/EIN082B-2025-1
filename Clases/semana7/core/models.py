from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField()

    def __str__(self):
        return self.codigo+"-"+self.nombre

