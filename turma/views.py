from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from turma.models import Turma
# Create your views here.

class Create_turma(CreateView):
    model = Turma
    template_name: str = 'turma/create_turma.html'
    fields = ['nome','ano','curso_turma','qtd_aulas_dia']

    def form_valid(self, form):
        return super().form_valid(form)