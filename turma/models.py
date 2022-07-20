from django.db import models
from curso.models import Curso

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.DateField()
    curso_turma = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
