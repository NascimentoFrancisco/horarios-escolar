from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from disponibilidade.models import Disponibilidade
from django.urls import reverse_lazy
# Create your views here.


def home_disponibilidade(request):
    return render(request, 'disponibilidade/home_disponibilidade.html')


class Create_dispnibilidade(CreateView):
    model = Disponibilidade
    template_name = 'disponibilidade/create_disponibilidade.html'
    fields = ['dia_semana',]
    success_url = reverse_lazy('disponibilidades:home_disponibilidade')

    def form_valid(self, form):
        return super().form_valid(form)