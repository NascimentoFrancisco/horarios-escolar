from django.db import models
from curso.models import Curso

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.CharField(max_length=10)#Neste campo será para o usuário digitar o ano da turma, por exemplo 2022.1
    curso_turma = models.ForeignKey(Curso,on_delete=models.CASCADE)
    qtd_aulas_dia = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
