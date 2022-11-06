from django.db import models

# Create your models here.
class Director(models.Model) :
    codigo = models.CharField('Codigo del director', primary_key=True, max_length=10)
    nombres = models.CharField('Nombres del director', max_length=150, null=False)
    apellidos = models.CharField('Apellidos del director', max_length=150, null=False)
    correo = models.EmailField('Correo del director', max_length=254, unique=True, null=False)

    def __str__(self):
        return "Director: "+self.nombres