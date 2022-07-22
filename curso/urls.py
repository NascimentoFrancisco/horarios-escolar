from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home_curso, name='home_curso'),
    path('registro/', views.Create_curso.as_view(), name='curso_cadastro'),   
]