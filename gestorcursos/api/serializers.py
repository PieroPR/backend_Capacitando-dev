from rest_framework import serializers
from gestorcursos.models import Curso, CursoUsuario, Sesion, Contenido, Recurso, contenido_vistas

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CursoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoUsuario
        fields = '__all__'

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = '__all__'

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = '__all__'

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'

class contenido_vistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = contenido_vistas
        fields = '__all__'
