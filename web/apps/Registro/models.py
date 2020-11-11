from django.db import models

# Create your models here.

class Mensaje(models.Model):
    email = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.TextField()
    telefono = models.CharField(max_length=50)
    gato = models.TextField()
    
    def __str__(self):
        return self.nombre