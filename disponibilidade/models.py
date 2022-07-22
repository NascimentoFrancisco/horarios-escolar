from django.db import models

# Create your models here.

class Disponibilidade(models.Model):
    DIAS_SEMANA = (
        ('SEGUNDA','Segunda-feira'),
        ('TERÇA','Terça-feira'),
        ('QUARTA','Quarta-feira'),
        ('QUINTA','Quinta-feira'),
        ('SEXTA','Sexta-feira'),
    )
    dia_semana = models.CharField(max_length=8,choices=DIAS_SEMANA)

    def __str__(self):
        return self.dia_semana
