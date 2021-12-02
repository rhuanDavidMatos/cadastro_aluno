from .models import AlunoModel

class AlunoService():
    
    def buscar_todos_alunos(self):
        return AlunoModel.objects.all()
    
    def buscar_por_nome(self, termo):
        return AlunoModel.objects.filter(nome__icontains=termo).order_by('nome')
    
    def buscar_aluno_por_id(self, id):
        return AlunoModel.objects.filter(id=id).first()
    
    def deletar_aluno_por_id(self, id):
        return AlunoModel.objects.filter(id=id).delete()