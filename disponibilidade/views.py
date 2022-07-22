from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from disponibilidade.models import Disponibilidade
# Create your views here.

class Create_dispnibilidade(CreateView):
    model = Disponibilidade
    template_name = 'disponibilidade/create_disponibilidade.html'
    fields = ['dia_semana',]

    def form_valid(self, form):
        return super().form_valid(form)