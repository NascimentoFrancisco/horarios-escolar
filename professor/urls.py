from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('home',views.Home_professor.as_view(),name='home_professor'),
    path('registro/', views.Create_professor.as_view(), name='create_professor'),
    path('lista/', views.List_professor.as_view(), name='list_professor'),   
    path('update/<int:pk>/', views.Update_professor.as_view(), name='update_professor'),
    path('delete/<int:pk>/', views.Delete_professor.as_view(), name='delete_professor'),      
]