from rest_framework import serializers
from gestorcursos.models import Curso, CursoUsuario, Sesion, Curso_Temas, Requisitos, Contenido, Recurso, contenido_vistas

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'portada', 'url_video_intro', 'url_portada_det', 'hora_duracion', 'total_clases', 'categoria', 'descripcion', 'fecha_inicio', 'fecha_final', 'estado', 'created_at', 'updated_at']

class CursoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoUsuario
        fields = ['id', 'id_curso', 'id_usuario']

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        fields = ['id', 'nombre_sesion', 'descripcion', 'id_curso', 'estado']

class Curso_TemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso_Temas
        fields = ['id', 'temas', 'estado']

class RequisitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisitos
        fields = ['id', 'id_curso', 'requisitos', 'estado']

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = ['id', 'id_seccion', 'titulo', 'descripcion', 'url_video', 'minutos_video', 'estado']

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ['id', 'id_contenido', 'nombre', 'tipo_recurso', 'url', 'archivo', 'estado']

class contenido_vistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = contenido_vistas
        fields = ['id', 'id_usuario', 'id_contenido', 'min_video']
