from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from aluno.serializers import AlunoSerializer
from curso.service import CursoService
from .models import AlunoModel
from endereco.models import EnderecoModel
from .service import AlunoService
from endereco.service import EnderecoService
from django.contrib import messages

_SERVICE = AlunoService()
_SERVICE_ENDERECO = EnderecoService()
_SERVICE_CURSO = CursoService()

def home(request):
    alunos = _SERVICE.buscar_todos_alunos()
    cursos = _SERVICE_CURSO.buscar_todos_cursos()
    return render(request, 'home.html', context={"alunos":alunos, "cursos":cursos})

def add_aluno(request):
    return render(request, 'add_aluno.html')

def salvar_aluno(request):
    serializer = AlunoSerializer(instance=AlunoModel(), data=request.POST)
    endereco = EnderecoModel()
    aluno = None
    if serializer.is_valid():
        aluno = serializer.save()

        endereco.logradouro = request.POST.get('logradouro')
        endereco.bairro = request.POST.get('bairro')
        endereco.numero = request.POST.get('numero')
        endereco.cidade = request.POST.get('cidade')
        endereco.estado = request.POST.get('estado')
        endereco.cep = request.POST.get('cep')
        endereco.aluno = aluno
        endereco.save()
        
        return HttpResponseRedirect('/')
    messages.error(request, serializer.errors)
    return render(request, 'add_aluno.html')
        
def deletar_aluno(request, id):
    _SERVICE.deletar_aluno_por_id(id)
    messages.success(request, "Aluno deletado!")
    return HttpResponseRedirect('/')
    
def editar_aluno(request, id):
    aluno = _SERVICE.buscar_aluno_por_id(id)
    endereco = _SERVICE_ENDERECO.buscar_endereco_por_aluno(id)
    return render(request, 'editar_aluno.html', context={"aluno":aluno, "endereco":endereco})

def update_aluno(request, id):
    aluno = _SERVICE.buscar_aluno_por_id(id)
    
    aluno.nome = request.POST.get('nome')
    aluno.email = request.POST.get('email')
    aluno.cpf = request.POST.get('cpf')
    aluno.telefone = request.POST.get('telefone')
    
    endereco = _SERVICE_ENDERECO.buscar_endereco_por_aluno(id)
    
    endereco.logradouro = request.POST.get('logradouro')
    endereco.numero = request.POST.get('numero')
    endereco.bairro = request.POST.get('bairro')
    endereco.cidade = request.POST.get('cidade')
    endereco.estado = request.POST.get('estado')
    endereco.cep = request.POST.get('cep')
    
    aluno.save()
    endereco.save()
    
    return HttpResponseRedirect('/')

def buscar_aluno(request):
    termo = request.GET.get('termo')
    alunos = _SERVICE.buscar_por_nome(termo)
    return render(request, template_name='home.html', context={'alunos': alunos})

def matricula_aluno(request, id):
    aluno = _SERVICE.buscar_aluno_por_id(id)
    cursos = _SERVICE_CURSO.buscar_todos_cursos()
    return render(request, template_name='matricular.html', context={'aluno': aluno, 'cursos': cursos})
    