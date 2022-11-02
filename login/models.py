
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import AspiranteManager


# Create your models here.

class Nacionalidad(models.Model):
    nombre = models.CharField('Pais', max_length=50)

    def __str__(self):
        return self.nombre

class Tipo_documento(models.Model):
    tipo_documento = models.CharField('Tipo de documento', max_length=50)

class Aspirante(AbstractBaseUser):
    documento = models.CharField('Documento de identidad', unique=True, max_length=100)
    codigo = models.CharField('Código de egresado', max_length=50)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    email_institucional = models.EmailField('Correo Institucional', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    foto = models.URLField('Foto de perfil', max_length=255)
    egresado_ufps = models.BooleanField(default=False)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['documento', 'email', 'email_institucional', 'nombres', 'apellidos', 'nacionalidad']

    def __str__(self):
        return " Aspirante "+ self.nombres+" "+self.apellidos+ " documento: "+self.documento