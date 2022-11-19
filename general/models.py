from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Tipo_documento(models.Model):
    tipo_documento = models.CharField('Tipo de documento', max_length=50)

#Maestria 
class Maestria(models.Model):
    codigo = models.CharField("Código", primary_key=True, max_length=10)
    nombre = models.CharField("Nombre", max_length=100)
    plazo_inicio = models.DateField("plazo_inicio")
    plazo_final = models.DateField("plazo_final")
    url_prueba = models.CharField("url_prueba", max_length=250)

    USERNAME_FIELD = 'codigo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return f"Director: {self.codigo}, nombre {self.nombre}"

class Aspirante(AbstractBaseUser):
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    documento = models.CharField('Documento de identidad', unique=True, max_length=100)
    foto = models.URLField('Foto de perfil', max_length=255)
    egresado_ufps = models.BooleanField('¿es egresado de la UFPS?', default=False)
    codigo = models.CharField('Código de egresado', max_length=50)
    es_extranjero = models.BooleanField('Extranjero', default=False)
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['documento', 'email', 'nombres', 'apellidos', 'es_extranjero']

    def __str__(self):
        return f"Aspirante: {self.documento} nombre: {self.nombres} {self.apellidos} email: {self.email}"

class Director(AbstractBaseUser):
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    correo = models.CharField('Correo', max_length=100)

    def __str__(self):
        return f"Director: {str(self.nombres+self.apellidos)}, correo {self.correo}"

#  Director_x_maestria
class DirectorXMaestria(models.Model):
    codigo_director_pk_fk = models.ForeignKey(Director, on_delete=models.CASCADE)
    codigo_maestria_pk_fk = models.ForeignKey(Maestria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_director_pk_fk} es director de la maestría -> {self.codigo_maestria_pk_fk}"

class Inscripcion():
    id_aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    pass