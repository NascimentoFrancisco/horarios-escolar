from django.urls import path
from . import views

app_name='disponibilidades'

urlpatterns = [
    path('home/',views.home_disponibilidade,name='home_disponibilidade'),
    path('registro/', views.Create_dispnibilidade.as_view(), name='create_disponibilidade'),   
    path('lista/', views.List_disponibilidade.as_view(), name='list_disponibilidade'),   
    path('update/<int:pk>/', views.Update_disponibilidade.as_view(), name='update_disponibilidade'),
    path('delete/<int:pk>/', views.Delete_disponibilidade.as_view(), name='delete_disponibilidade'),         
]