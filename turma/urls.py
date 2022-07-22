from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.Create_turma.as_view(), name='curso_cadastro'),   
]