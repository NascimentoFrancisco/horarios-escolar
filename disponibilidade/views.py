from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from disponibilidade.models import Disponibilidade
from django.urls import reverse_lazy
# Create your views here.


def home_disponibilidade(request):
    return render(request, 'disponibilidade/home_disponibilidade.html')


class Create_dispnibilidade(CreateView):
    model = Disponibilidade
    template_name = 'disponibilidade/create_disponibilidade.html'
    fields = ['dia_semana',]
    success_url = reverse_lazy('disponibilidades:list_disponibilidade')

    def form_valid(self, form):
        return super().form_valid(form)

class List_disponibilidade(ListView):
    template_name: str = 'disponibilidade/list_disponibilidade.html'

    def get_queryset(self):
        queryset = Disponibilidade.objects.all()
        return queryset

class Update_disponibilidade(UpdateView):    
    model =Disponibilidade
    template_name = 'disponibilidade/create_disponibilidade.html'
    fields = ['dia_semana',]
    success_url = reverse_lazy('disponibilidades:list_disponibilidade')

    def form_valid(self, form):
        return super().form_valid(form)

class Delete_disponibilidade(DeleteView):
    model =Disponibilidade
    template_name = 'disponibilidade/delete_disponibilidade.html'
    success_url = reverse_lazy('disponibilidades:list_disponibilidade')

    def get_success_url(self):
        return reverse_lazy('disponibilidades:list_disponibilidade')
