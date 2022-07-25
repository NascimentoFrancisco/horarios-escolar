from django.shortcuts import render
from curso.models import Curso
from django.views.generic import CreateView, UpdateView,ListView
from django.urls import reverse_lazy
# Create your views here.

def home_curso(request):
    return render(request, 'curso/home_curso.html')

class Create_curso(CreateView):
    model = Curso
    template_name = 'curso/create_curso.html'
    fields = ['nome',]
    success_url = reverse_lazy('cursos:home_curso')

    def form_valid(self, form):
        return super().form_valid(form)

create_curso = Create_curso.as_view()