from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from aluno.service import AlunoService
from curso.service import CursoService
from matricula.serializers import MatriculaSerializer

_SERVICE_ALUNO = AlunoService()
_SERVICE_CURSO = CursoService()

def matricular(request, id):
    aluno = _SERVICE_ALUNO.buscar_aluno_por_id(request.POST.get("id_aluno"))
    curso = _SERVICE_CURSO.buscar_curso_por_id(id)
    
    data = {
        "aluno": aluno.id,
        "curso": curso.id,
        "data_inicio": request.POST.get("data_inicio"),
        "data_fim": request.POST.get("data_fim"),
    }
    serializer = MatriculaSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        return HttpResponseRedirect('/')
    cursos = _SERVICE_CURSO.buscar_todos_cursos()
    return render(request, template_name='matricular.html', context={'aluno': aluno, 'cursos': cursos})