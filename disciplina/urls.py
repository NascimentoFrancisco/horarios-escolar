from django.urls import path
from . import views

app_name = 'disciplinas'

urlpatterns = [
    path('home/',views.home_disciplina, name='home_disciplina'),
    path('registro/', views.Create_disciplina.as_view(), name='create_disciplina'),
    path('lista/', views.List_disciplina.as_view(), name='list_disciplina'),   
    path('update/<int:pk>/', views.Update_disciplina.as_view(), name='update_disciplina'),
    path('delete/<int:pk>/', views.Delete_disciplina.as_view(), name='delete_disciplina'),      
]