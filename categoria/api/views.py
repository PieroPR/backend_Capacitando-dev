from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer

class CategoriaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()