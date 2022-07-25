from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('home',views.home_professor,name='home_professor'),
    path('registro/', views.Create_professor.as_view(), name='create_professor'),   
]