from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from turma.models import Turma
from django.urls import reverse_lazy
# Create your views here.

def home_turma(request):
    return render(request, 'turma/home_turma.html')

class Create_turma(CreateView):
    model = Turma
    template_name: str = 'turma/create_turma.html'
    fields = ['nome','ano','curso_turma','qtd_aulas_dia','disciplinas_turma']
    success_url = reverse_lazy('turmas:home_turma')

    def form_valid(self, form):
        return super().form_valid(form)