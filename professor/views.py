from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,ListView,DeleteView
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

class List_professor(ListView):
    template_name: str = 'professor/list_professor.html'

    def get_queryset(self):
        queryset = Professor.objects.all()
        return queryset

class Update_professor(UpdateView):    
    model =Professor
    template_name = 'professor/create_professor.html'
    fields = ['nome','suap','coordenador','disponibilidade_professor','email','telefone']
    success_url = reverse_lazy('professores:list_professor')

    def form_valid(self, form):
        return super().form_valid(form)

class Delete_professor(DeleteView):
    model =Professor
    template_name = 'professor/delete_professor.html'
    success_url = reverse_lazy('professores:list_professor')

    def get_success_url(self):
        return reverse_lazy('professores:list_professor')
