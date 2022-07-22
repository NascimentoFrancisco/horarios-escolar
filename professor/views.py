from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from professor.models import Professor
# Create your views here.


class Create_professor(CreateView):
    model = Professor
    template_name = 'professor/create_professor.html'
    fields = ['nome','suap','coordenador','disponibilidade_professor','email','telefone']

    def form_valid(self, form):
        return super().form_valid(form)