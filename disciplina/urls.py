from django.urls import path
from . import views

app_name = 'disciplinas'

urlpatterns = [
    path('home/',views.home_disciplina, name='home_disciplina'),
    path('registro/', views.Create_disciplina.as_view(), name='create_disciplina'),   
]