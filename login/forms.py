from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from general.models import Aspirante

class RegistrarAspirante(UserCreationForm):
    #form de registro aspirante
    nombres = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={"autofocus": True}))
    apellidos = forms.CharField(label='Apellidos', required=True)
    documento = forms.CharField(label='Documento', max_length=15, required=True)
    foto = forms.ImageField(required=False)
    username = forms.EmailField(label='Correo', required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), required=True)
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), required=True)
    egresado_ufps = forms.BooleanField(required=False)
    es_extranjero = forms.BooleanField(required=False)
    

    class Meta:
        model=User
        fields = ['nombres', 'apellidos', 'documento','username', 'foto', 'password1', 'password2','egresado_ufps', 'es_extranjero']
        help_texts = {k:"" for k in fields}

class LoginAspirante(forms.Form):
    username = forms.EmailField(label='Correo', required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), required=True)

class RegistrarDirector(forms.Form):
    #form de registro director
    #todos los campos aquí
    pass