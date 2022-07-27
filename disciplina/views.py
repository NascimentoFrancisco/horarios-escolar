from django.shortcuts import render
from django.views.generic import View,CreateView, UpdateView,ListView, DeleteView
from disciplina.models import Disciplina
from django.urls import reverse_lazy
# Create your views here.

class Home_disciplina(View):
    
    def get(self, request):
        return render(request, 'disciplina/home_disciplina.html')

class Create_disciplina(CreateView):
    model = Disciplina
    template_name = 'disciplina/create_disciplina.html'
    fields = ['nome','carga_horaria','aulas_por_semana','curso_disciplina','profesor_disciplina']
    success_url = reverse_lazy('disciplinas:list_disciplina')

    def form_valid(self, form):
        return super().form_valid(form)

class Update_disciplina(UpdateView):
    model = Disciplina
    template_name: str = 'disciplina/create_disciplina.html'
    fields = ['nome','carga_horaria','aulas_por_semana','curso_disciplina','profesor_disciplina']
    success_url = reverse_lazy('disciplinas:list_disciplina')

    def form_valid(self, form):
        return super().form_valid(form)

class List_disciplina(ListView):
    template_name: str = 'disciplina/list_disciplina.html'

    def get_queryset(self):
        queryset = Disciplina.objects.all()
        return queryset

class Delete_disciplina(DeleteView):
    model =Disciplina
    template_name = 'disciplina/delete_disciplina.html'
    success_url = reverse_lazy('disciplinas:list_disciplina')

    def get_success_url(self):
        return reverse_lazy('disciplinas:list_disciplina')