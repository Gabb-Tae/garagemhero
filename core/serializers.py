from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

from core.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

from core.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"