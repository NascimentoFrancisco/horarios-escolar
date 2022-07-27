from django.shortcuts import render
from django.views.generic import View,CreateView, UpdateView,ListView,DeleteView
from turma.models import Turma
from django.urls import reverse_lazy
# Create your views here.

class Home_turma(View):
    
    def get(self, request):
        return render(request, 'turma/home_turma.html')

class Create_turma(CreateView):
    model = Turma
    template_name: str = 'turma/create_turma.html'
    fields = ['nome','ano','curso_turma','qtd_aulas_dia','disciplinas_turma']
    success_url = reverse_lazy('turmas:home_turma')

    def form_valid(self, form):
        return super().form_valid(form)
    
class List_turma(ListView):
    template_name: str = 'turma/list_turma.html'

    def get_queryset(self):
        queryset = Turma.objects.all()
        return queryset

class Update_turma(UpdateView):    
    model =Turma
    template_name = 'turma/create_turma.html'
    fields = ['nome','ano','curso_turma','qtd_aulas_dia','disciplinas_turma']
    success_url = reverse_lazy('turmas:list_turma')

    def form_valid(self, form):
        return super().form_valid(form)

class Delete_turma(DeleteView):
    model =Turma
    template_name = 'turma/delete_turma.html'
    success_url = reverse_lazy('turmas:list_turma')

    def get_success_url(self):
        return reverse_lazy('turmas:list_turma')
