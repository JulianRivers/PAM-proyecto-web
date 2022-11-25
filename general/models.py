from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.

class Tipo_documento(models.Model):
    tipo_documento = models.CharField('Tipo de documento', max_length=50)

#Maestria 
class Maestria(models.Model):
    codigo = models.CharField("Código", primary_key=True, max_length=10)
    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.CharField("Descripción", max_length=255)
    imagen = models.CharField("imagen", max_length=50)
    plazo_inicio = models.DateField("plazo inicio")
    plazo_final = models.DateField("plazo final")
    url_prueba = models.CharField("url prueba", max_length=250)

    USERNAME_FIELD = 'codigo'
    REQUIRED_FIELDS = ['codigo', 'nombre', 'descripcion', 'imagen']

    def __str__(self):
        return f"{self.nombre}, {self.codigo}"

class Aspirante(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
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

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = [ 'email', 'nombres', 'apellidos']
    def __str__(self):
        return f"Director: {str(self.nombres+self.apellidos)}, correo {self.correo}"

#  Director_x_maestria
class DirectorXMaestria(models.Model):
    codigo_director_pk_fk = models.ForeignKey(Director, on_delete=models.CASCADE)
    codigo_maestria_pk_fk = models.ForeignKey(Maestria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_director_pk_fk} es director de la maestría -> {self.codigo_maestria_pk_fk}"

class Cohorte(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    fecha_inicio = models.DateField('Fecha de inicio', max_length=255)
    fecha_finalizacion =  models.DateField('Fecha de finalización', max_length=255)
    cupos_aprobados = models.IntegerField('Cupos aprobados', default=0)
    cupos_asignados = models.IntegerField('Cupos asignados', default=0)
    
    def __str__(self):
        return f"{self.nombre}"
    
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['nombre', 'fecha_inicio', 'fecha_finalizacion', 'cupos_aprobados', 'cupos_asignados']
    
class Inscripcion(models.Model):
    id_aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    id_maestria = models.ForeignKey(Maestria, on_delete=models.CASCADE)
    id_cohorte = models.ForeignKey(Cohorte, on_delete=models.CASCADE)
    estado_pago = models.BooleanField('Estado del pago', default=False)
    doc_entrevista = models.URLField('Documento de entrevista', max_length=255)
    calificacion_entrevista = models.IntegerField('Calificación de entrevista', default=0)
    doc_prueba = models.URLField('Documento de prueba', max_length=255)
    calificacion_prueba = models.IntegerField('Calificación de prueba', default=0)
    doc_hoja_vida = models.URLField('Documento de hoja de vida', max_length=255)
    calificacion_cv = models.IntegerField('Calificación de hoja de vida', default=0)
    copia_diploma_pregrado = models.URLField('Documento de diploma de pregrado', max_length=255)
    copia_notas_acta = models.URLField('Documento de notas y acta de grado', max_length=255)
    copia_pasaporte_visa = models.URLField('Documento de pasaporte y visa', max_length=255)
    notas_apostillada = models.URLField('Documento de notas apostillada', max_length=255)
    diploma_apostillado = models.URLField('Documento de diploma apostillado', max_length=255)
    doc_pago_inscripcion = models.URLField('Documento de pago de inscripción', max_length=255)
    fecha_entrevista = models.DateField('Fecha de entrevista', max_length=255)
    puntaje_total = models.IntegerField('Puntaje total', default=0)
    fotocopia_cedula = models.URLField('Documento de fotocopia de cédula', max_length=255)
    url_prueba = models.URLField('Documento de prueba', max_length=255)
    url_entrevista = models.URLField('Documento de entrevista', max_length=255)
    
    def __str__(self):
        return f"Inscripción: {self.id_aspirante} - {self.id_maestria}"
    
class carta_referencia(models.Model):
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    calificacion = models.IntegerField('Calificación', default=0)
    documento = models.URLField('Documento', max_length=255)
    
    def __str__(self):
        return f"Carta de referencia: {self.id_inscripcion}"
    