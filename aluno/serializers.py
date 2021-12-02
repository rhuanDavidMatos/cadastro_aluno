from .models import AlunoModel
from rest_framework import serializers

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = ('id','nome', 'email', 'cpf', 'telefone')