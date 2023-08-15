from django.db import models

# Create your models here.

class Usuario(models.Model):
    # no agregamos id porque django lo crea automaticamente
    usuario = models.CharField(max_length=80)
    password = models.CharField(max_length=300)
    estado = models.BooleanField('Estado', default=True)
    rol = models.IntegerField()
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=9)
    dni = models.CharField(max_length=7)
    correo = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    foto = models.CharField(max_length=250)
    carrera = models.CharField(max_length=250)
    perfil = models.TextField()
    # OK
