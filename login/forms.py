from django import forms

class RegistrarAspirante(forms.Form):
    documento = forms.CharField(label='Documento', max_length=100)
    codigo = forms.CharField(label='Código', max_length=50)
    email = forms.EmailField(label='Correo', required=False)
    email_institucional = forms.EmailField(label='Correo_Institucional', required=False)
    nombres = forms.CharField(label='Nombres', required=False)
    apellidos = forms.CharField(label='Apellidos', required=True)
    foto = forms.CharField(label='Foto de perfil')
    egresado_ufps = forms.BooleanField()
    nacionalidad = forms.IntegerField()
