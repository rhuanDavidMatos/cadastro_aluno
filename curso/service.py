from .models import CursoModel

class CursoService():
    
    def buscar_todos_cursos(self):
        return CursoModel.objects.all()
    
    def buscar_curso_por_id(self, id):
        return CursoModel.objects.filter(id=id).first()