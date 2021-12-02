from .models import MatriculaModel
from rest_framework import serializers

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaModel
        fields = ('aluno', 'curso', 'data_inicio', 'data_fim')
