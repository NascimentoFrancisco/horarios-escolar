from django.db import models
from disponibilidade.models import Disponibilidade
# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    suap = models.CharField(max_length=100, unique=True)
    coordenador = models.BooleanField(default=False)
    disponibilidade_professor = models.ManyToManyField(Disponibilidade)
    email = models.EmailField()
    telefone = models.CharField(max_length=16)

    def __str__(self):
        return self.nome
