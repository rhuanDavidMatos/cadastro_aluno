from django.urls import path
from .views import add_aluno, home, salvar_aluno, deletar_aluno, editar_aluno, update_aluno, buscar_aluno, matricula_aluno

urlpatterns = [
    path('', home, name="home"),
    path('add_aluno/', add_aluno, name="add_aluno"),
    path('salvar_aluno/', salvar_aluno, name="salvar_aluno"),
    path('deletar_aluno/<id>/', deletar_aluno, name="deletar_aluno"),
    path('editar_aluno/<id>/', editar_aluno, name="editar_aluno"),
    path('update_aluno/<id>', update_aluno, name="update_aluno"),
    path('matricula_aluno/<id>', matricula_aluno, name="matricula_aluno"),
    path('buscar/', buscar_aluno, name="buscar_aluno"),
]