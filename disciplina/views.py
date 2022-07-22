from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from disciplina.models import Disciplina
# Create your views here.

class Create_disciplina(CreateView):
    model = Disciplina
    template_name = 'disciplina/create_disciplina.html'
    fields = ['nome','carga_horaria','aulas_por_semana','curso_disciplina','profesor_disciplina']

    def form_valid(self, form):
        return super().form_valid(form)
