
from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('cursos/',include('curso.urls')),
    path('professores/',include('professor.urls')),
    path('disciplinas/',include('disciplina.urls')),
    path('disponibilidades/',include('disponibilidade.urls')),
    path('turmas/',include('turma.urls')),
]
