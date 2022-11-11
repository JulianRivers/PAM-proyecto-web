from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.messages.api import success
from login.forms import *
from login.models import Aspirante


# Create your views here.
def index(request):
    form = LoginAspirante()
    return render(request, 'aspirante/login_a.html', {'form':form})

def director(request):
    return render(request, 'director/login_d.html')

def registrar_a(request):
    return render(request, 'aspirante/registrar_a.html', {'form': RegistrarAspirante()})

def guardar_a(request):
    #Registra Aspirantes
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    documento = request.POST['documento']
    #foto = request.POST['foto'] #aún no
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
    success(request, F"Bienvenido {nombres}")
    login(request, aspirante)
    return redirect('/aspirante/inicio')

#login
def ingresar_a(request):
    email = request.POST.get('email', False)
    password = request.POST.get('password', False)
    usuario = authenticate(email=email, password=password)
    if usuario is not None:
        login(request, usuario)
        return redirect('/aspirante/inicio')
    else:
        return redirect('/')
