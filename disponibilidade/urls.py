from django.urls import path
from . import views

app_name='disponibilidades'

urlpatterns = [
    path('home/',views.home_disponibilidade,name='home_disponibilidade'),
    path('registro/', views.Create_dispnibilidade.as_view(), name='create_disponibilidade'),   
]