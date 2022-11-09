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
    return render(request, 'registrarse.html', {'form': RegistrarAspirante()})


def registrarAspirante(request):
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    documento = request.POST['documento']
    #foto = request.POST['foto']
    email = request.POST['email']
    password = request.POST['password']
    if request.POST.get('egresado_ufps', False) == "on" :
        egresado_ufps = True
    else: 
        egresado_ufps = False
    if request.POST.get('es_extranjero', False) == "on":
        es_extranjero = True
    else: 
        es_extranjero = False

    aspirante = Aspirante.objects.create(
        nombres=nombres, apellidos=apellidos, documento=documento, email=email, 
        password=password, egresado_ufps=egresado_ufps, es_extranjero=es_extranjero)
    return redirect('/')
