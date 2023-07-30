from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from usuario.models import Usuario
from usuario.api.serializers import UsuarioSerializer

class UsuarioApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()