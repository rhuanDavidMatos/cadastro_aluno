from django.db import models

class CursoModel(models.Model):

    nome=models.CharField(max_length=100, unique=True)

    horas=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.nome}; {self.horas}"