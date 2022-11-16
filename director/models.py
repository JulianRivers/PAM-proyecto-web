from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Director(AbstractBaseUser):
    #Campos de la base de datos o atributos del objeto :)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    correo = models.CharField('Correo', max_length=100)

    def __str__(self):
        return f"Director: {str(self.nombres+self.apellidos)}, correo {self.correo}"

#Maestria 
class Maestria():
    codigo = models.CharField("codigo", primary_key=True)
    nombre = models.CharField("nombre", max_length=100)
    plazo_inicio = models.DateField("plazo_inicio" )
    plazo_final = models.DateField("plazo_final")
    url_prueba = models.CharField("url_prueba", max_length=250)


#  Director_x_maestria
class DirectorXMaestria(models.Model):
    codigo_director_pk_fk = models.ForeignKey(Director, on_delete=models.CASCADE)
    codigo_maestria_pk_fk = models.ForeignKey(Maestria, on_delete=models.CASCADE)