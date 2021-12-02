from .models import EnderecoModel
from rest_framework import serializers

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoModel
        fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'aluno')
