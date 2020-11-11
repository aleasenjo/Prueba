from django.db import models

# Create your models here.

class Gato (models.Model):
    fotografia = models.ImageField(upload_to='gatos')
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.fotografia)
