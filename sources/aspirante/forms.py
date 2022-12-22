from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditarInformacion(forms.Form):
    #form de editar la informacion aspirante
    nombres = forms.CharField(label='Nombres', required=False, widget=forms.TextInput(attrs={"autofocus": True}))
    apellidos = forms.CharField(label='Apellidos', required=False)
    documento = forms.CharField(label='Documento', max_length=15, required=False)
    foto = forms.ImageField(label='Foto', required=False)
