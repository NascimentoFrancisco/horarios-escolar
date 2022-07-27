from django.shortcuts import render
from curso.models import Curso
from django.views.generic import View,CreateView, UpdateView,ListView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Home_curso(View):
    
    def get(self, request):
        return render(request, 'curso/home_curso.html')

class Create_curso(CreateView):
    model = Curso
    template_name = 'curso/create_curso.html'
    fields = ['nome',]
    success_url = reverse_lazy('cursos:list_curso')

    def form_valid(self, form):
        return super().form_valid(form)

class Update_curso(UpdateView):
    model = Curso
    template_name: str = 'curso/create_curso.html'
    fields = ['nome',]
    success_url = reverse_lazy('cursos:list_curso')

    def form_valid(self, form):
        return super().form_valid(form)

class List_curso(ListView):
    template_name: str = 'curso/list_curso.html'

    def get_queryset(self):
        queryset = Curso.objects.all()
        return queryset

class Delete_curso(DeleteView):
    model =Curso
    template_name = 'curso/delete_curso.html'
    success_url = reverse_lazy('cursos:list_curso')

    def get_success_url(self):
        return reverse_lazy('cursos:list_curso')