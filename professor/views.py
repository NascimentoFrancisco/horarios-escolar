from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from professor.models import Professor
from django.urls import reverse_lazy
# Create your views here.


def home_professor(request):
    return render(request, 'professor/home_professor.html')


class Create_professor(CreateView):
    model = Professor
    template_name = 'professor/create_professor.html'
    fields = ['nome','suap','coordenador','disponibilidade_professor','email','telefone']
    success_url = reverse_lazy('professores:home_professor')

    def form_valid(self, form):
        return super().form_valid(form)