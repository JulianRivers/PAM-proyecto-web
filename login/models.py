
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import AspiranteManager


# Create your models here.

class Tipo_documento(models.Model):
    tipo_documento = models.CharField('Tipo de documento', max_length=50)

class Aspirante(AbstractBaseUser):
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    documento = models.CharField('Documento de identidad', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    #foto = models.URLField('Foto de perfil', max_length=255)
    egresado_ufps = models.BooleanField('¿es egresado de la UFPS?', default=False)
    codigo = models.CharField('Código de egresado', max_length=50)
    es_extranjero = models.BooleanField('Extranjero', default=False)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['documento', 'email', 'nombres', 'apellidos', 'es_extranjero']

    def __str__(self):
        return " Aspirante "+self.nombres+" "+self.apellidos+ " documento: "+self.documento