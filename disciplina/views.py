from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from disciplina.models import Disciplina
from django.urls import reverse_lazy
# Create your views here.

def home_disciplina(request):
    return render(request, 'disciplina/home_disciplina.html')

class Create_disciplina(CreateView):
    model = Disciplina
    template_name = 'disciplina/create_disciplina.html'
    fields = ['nome','carga_horaria','aulas_por_semana','curso_disciplina','profesor_disciplina']
    success_url = reverse_lazy('disciplinas:home_disciplina')

    def form_valid(self, form):
        return super().form_valid(form)
