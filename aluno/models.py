from django.db import models

class AlunoModel(models.Model):

    nome = models.CharField(
        max_length=100,
    )

    email = models.EmailField(
        unique=True
    )

    cpf = models.CharField(
        max_length=14,
        unique=True,
    )

    telefone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.nome}"