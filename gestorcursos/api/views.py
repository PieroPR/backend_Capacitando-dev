from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from gestorcursos.models import Curso, CalificacionCurso, CursoUsuario, Seccion, Curso_Temas, Requisitos, Clase, Recurso, clases_vistas, Examen, Pregunta, Alternativa, ResolverExamen, DetalleResolverExamen, Respuesta
from gestorcursos.api.serializers import CursoSerializer, CalificacionCursoSerializer, CursoUsuarioSerializer, SeccionSerializer, Curso_TemasSerializer, RequisitosSerializer, ClaseSerializer, RecursoSerializer, clases_vistasSerializer, ExamenSerializer, PreguntaSerializer, AlternativaSerializer, ResolverExamenSerializer, DetalleResolverExamenSerializer, RespuestaSerializer


class CursoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class CalificacionCursoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CalificacionCursoSerializer
    queryset = CalificacionCurso.objects.all()

class CursoUsuarioApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoUsuarioSerializer
    queryset = CursoUsuario.objects.all()

class SeccionApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()

class Curso_TemasApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = Curso_TemasSerializer
    queryset = Curso_Temas.objects.all()

class RequisitosApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = RequisitosSerializer
    queryset = Requisitos.objects.all()

class ClaseApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ClaseSerializer
    queryset = Clase.objects.all()

class RecursoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = RecursoSerializer
    queryset = Recurso.objects.all()

class clases_vistasApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = clases_vistasSerializer
    queryset = clases_vistas.objects.all()

class ExamenApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ExamenSerializer
    queryset = Examen.objects.all()

class PreguntaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = PreguntaSerializer
    queryset = Pregunta.objects.all()

class AlternativaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = AlternativaSerializer
    queryset = Alternativa.objects.all()

class ResolverExamenApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ResolverExamenSerializer
    queryset = ResolverExamen.objects.all()

class DetalleResolverExamenApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = DetalleResolverExamenSerializer
    queryset = DetalleResolverExamen.objects.all()

class RespuestaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = RespuestaSerializer
    queryset = Respuesta.objects.all()






