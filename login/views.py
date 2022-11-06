from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from login.forms import RegistrarAspirante
from login.models import Aspirante


# Create your views here.
def index(request):
    return render(request, 'loginAspirante.html')

def director(request):
    return render(request, 'logindirector.html')

def registrar_aspirante(request):
    return render(request, 'registrarse.html', {'form':RegistrarAspirante()})

#no sirve
def inicio(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data("email")
            documento = form.cleaned_data("documento")
            password = form.cleaned_data("password")
            usuario = authenticate(email=correo, documento=documento, password=password)
            if usuario is not None:
                login(request, login)
                return redirect('prueba')