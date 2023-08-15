from rest_framework import serializers
from categoria.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Categoria
        fields = ['id', 'categoria','estado']
        # OK