from django.urls import path
from . import views

app_name = "turmas"

urlpatterns = [
    path('home/',views.Home_turma.as_view(),name='home_turma'),
    path('registro/', views.Create_turma.as_view(), name='create_turma'),
    path('lista/', views.List_turma.as_view(), name='list_turma'),   
    path('update/<int:pk>/', views.Update_turma.as_view(), name='update_turma'),
    path('delete/<int:pk>/', views.Delete_turma.as_view(), name='delete_turma'),            
]