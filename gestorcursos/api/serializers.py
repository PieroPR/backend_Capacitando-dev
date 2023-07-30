from rest_framework import serializers
from gestorcursos.models import Curso, CalificacionCurso, CursoUsuario, Seccion, Curso_Temas, Requisitos, Clase, Recurso, clases_vistas, Examen, Pregunta, Alternativa, ResolverExamen, DetalleResolverExamen, Respuesta

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'portada', 'url_video_intro', 'url_portada_det', 'hora_duracion', 'total_clases', 'categoria', 'descripcion', 'fecha_inicio', 'fecha_final', 'estado', 'created_at', 'updated_at']

class CalificacionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionCurso
        fields = ['id', 'id_curso', 'id_usuario', 'pregunta1', 'pregunta2', 'pregunta3','pregunta4','pregunta5','pregunta6','pregunta7','pregunta8','pregunta9','pregunta10','promedio_calificacion']
    
class CursoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoUsuario
        fields = ['id', 'id_curso', 'id_usuario']

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ['id', 'nombre_seccion', 'descripcion', 'id_curso', 'estado']

class Curso_TemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso_Temas
        fields = ['id', 'temas', 'estado']

class RequisitosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisitos
        fields = ['id', 'id_curso', 'requisitos', 'estado']

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'id_seccion', 'titulo', 'descripcion', 'url_video', 'minutos_video', 'estado']

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ['id', 'id_clase', 'nombre', 'tipo_recurso', 'url', 'archivo', 'estado']

class clases_vistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = clases_vistas
        fields = ['id', 'id_usuario', 'id_clase', 'nombre', 'tipo_recurso']

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = ['id', 'titulo', 'descripcion', 'id_seccion', 'estado']

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id', 'id_examen', 'nombre', 'puntos', 'estado']

class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['id', 'id_pregunta', 'nombre', 'estado', 'correcta']

class ResolverExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolverExamen
        fields = ['id', 'id_usuario', 'id_examen', 'calificacion_total', 'calificacion_final', 'notas', 'examen_terminado', 'estado']

class DetalleResolverExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleResolverExamen
        fields = ['id', 'id_resolver_examen', 'id_pregunta', 'id_alternativa', 'estado']

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = ['id', 'id_pregunta', 'id_alternativa', 'id_usuario']