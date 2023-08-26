from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from gestorcursos.models import Curso, CursoUsuario, Sesion, Contenido, Recurso, contenido_vistas
from gestorcursos.api.serializers import CursoSerializer, CursoUsuarioSerializer, SesionSerializer, ContenidoSerializer, RecursoSerializer, contenido_vistasSerializer


class CursoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    # OK

class CursoUsuarioApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CursoUsuarioSerializer
    queryset = CursoUsuario.objects.all()
    # OK

class SesionApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SesionSerializer
    queryset = Sesion.objects.all()
    # OK

class ContenidoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ContenidoSerializer
    queryset = Contenido.objects.all()
    # OK

class RecursoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = RecursoSerializer
    queryset = Recurso.objects.all()
    # OK

class contenido_vistasApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = contenido_vistasSerializer
    queryset = contenido_vistas.objects.all()
    # OK






