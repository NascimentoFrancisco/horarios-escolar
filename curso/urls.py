from django.urls import path
from . import views

app_name = "cursos"

urlpatterns = [
    path('home',views.home_curso, name='home_curso'),
    path('registro/', views.create_curso, name='create_curso'),   
]