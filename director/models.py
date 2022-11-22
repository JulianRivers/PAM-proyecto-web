from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Director(AbstractBaseUser):
    #Campos de la base de datos o atributos del objeto :)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    correo = models.CharField('Correo', max_length=100)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nombre', "apellidos","correo"]

    def __str__(self):
        return f"Director: {str(self.nombres+self.apellidos)}, correo {self.correo}"

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

#  Director_x_maestria
class DirectorXMaestria(models.Model):
    codigo_director_pk_fk = models.ForeignKey(Director, on_delete=models.CASCADE)
    codigo_maestria_pk_fk = models.ForeignKey(Maestria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_director_pk_fk} es director de la maestría -> {self.codigo_maestria_pk_fk}"

