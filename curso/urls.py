from django.urls import path
from . import views

app_name = "cursos"

urlpatterns = [
    path('home',views.home_curso, name='home_curso'),
    path('registro/', views.Create_curso.as_view(), name='create_curso'),   
    path('lista/', views.List_curso.as_view(), name='list_curso'),   
    path('update/<int:pk>/', views.Update_curso.as_view(), name='update_curso'),   
    path('delete/<int:pk>/', views.Delete_curso.as_view(), name='delete_curso'),   
]