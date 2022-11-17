from django.db import models
from director.models import *
from login.models import *#importamos para las llaves primarias
# Create your models here.
class Inscripcion():
    id_aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    pass