from django.db import models
from aluno.models import AlunoModel
from curso.models import CursoModel

class MatriculaModel(models.Model):

    aluno = models.ForeignKey(
        AlunoModel,
        on_delete=models.DO_NOTHING
    )

    curso = models.ForeignKey(
        CursoModel,
        on_delete=models.DO_NOTHING
    )

    data_inicio = models.DateField()

    data_fim = models.DateField()

    def __str__(self) -> str:
        return f"Inicio: {self.data_inicio}; Fim: {self.data_fim}"