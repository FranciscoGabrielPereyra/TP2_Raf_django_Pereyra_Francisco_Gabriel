from django.db import models

# Proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=200)
    empresa = models.CharField(max_length=100)
    sitio_web = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.empresa}"

