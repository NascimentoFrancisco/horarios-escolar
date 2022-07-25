
from django.contrib import admin
from django.urls import path 
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('cursos/',include('curso.urls',namespace="cursos")),
    path('professores/',include('professor.urls',namespace='professores')),
    path('disciplinas/',include('disciplina.urls',namespace='disciplinas')),
    path('disponibilidades/',include('disponibilidade.urls',namespace='disponibilidades')),
    path('turmas/',include('turma.urls',namespace="turmas")),
]
