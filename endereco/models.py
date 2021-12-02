from django.db import models
from aluno.models import AlunoModel

class EnderecoModel(models.Model):

    logradouro = models.CharField(max_length=200)

    numero = models.CharField(max_length=8)

    bairro = models.CharField(max_length=30)

    cidade = models.CharField(max_length=30)

    estado = models.CharField(max_length=2)

    cep = models.CharField(max_length=9)

    aluno = models.ForeignKey(
        AlunoModel,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.id}"