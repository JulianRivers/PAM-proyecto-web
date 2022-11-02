from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  

# Create your models here.

#mirar nulos 
class Aspirante(AbstractBaseUser):
    documento = models.CharField('Documento de identidad', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True, null=False)
    nombres = models.CharField('Nombres', max_lenght=150, null=False)
    apellidos = models.CharField('Apellidos', max_lenght=150, null=False)
    foto = models.CharField('Foto de perfil', max_length=None)