from django.urls import path
from . import views

app_name = "turmas"

urlpatterns = [
    path('home/',views.home_turma,name='home_turma'),
    path('registro/', views.Create_turma.as_view(), name='create_turma'),   
]