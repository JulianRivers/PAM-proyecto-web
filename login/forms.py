from django import forms

class RegistrarAspirante(forms.Form):
    #form de registro aspirante
    nombres = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={"autofocus": True}))
    apellidos = forms.CharField(label='Apellidos', required=True)
    documento = forms.CharField(label='Documento', max_length=15, required=True)
    foto = forms.ImageField(required=True)
    email = forms.EmailField(label='Correo', required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), required=True)
    egresado_ufps = forms.BooleanField(required=False)
    es_extranjero = forms.BooleanField(required=False)

class LoginAspirante(forms.Form):
    email = forms.EmailField(label='Correo', required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}), required=True)

class RegistrarDirector(forms.Form):
    #form de registro director
    #todos los campos aquí
    pass