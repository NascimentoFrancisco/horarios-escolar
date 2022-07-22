from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length=50, unique=True, error_messages={'unique' : "Usuário já cadastrado!"})
    password = models.CharField(max_length=5)
    email = models.EmailField(max_length=245, unique=True,error_messages={'unique' : "Email já cdastrado!"})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
