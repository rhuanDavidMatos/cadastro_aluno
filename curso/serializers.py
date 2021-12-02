from .models import CursoModel
from rest_framework import serializers

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoModel
        fields = ('id', 'nome', 'horas')