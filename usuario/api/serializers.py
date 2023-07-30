from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'password', 'estado', 'rol', 'nombre', 'apellido', 'telefono', 'dni', 'correo', 'direccion', 'foto', 'carrera', 'perfil']
