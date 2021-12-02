from endereco.serializers import EnderecoSerializer
from .models import EnderecoModel

class EnderecoService():
    
    def salvar_endereco(self, id):
        serializer = EnderecoSerializer()
        return None
    
    def buscar_endereco_por_aluno(self, id):
        return EnderecoModel.objects.filter(aluno_id=id).first()