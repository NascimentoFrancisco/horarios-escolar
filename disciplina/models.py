from django.db import models
from professor.models import Professor
from curso.models import Curso
# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    aulas_por_semana = models.IntegerField()#Para definir a quantidade de aulas por semana
    curso_disciplina = models.ForeignKey(Curso,on_delete=models.CASCADE)
    profesor_disciplina = models.ForeignKey(Professor,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
