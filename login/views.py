from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.messages.api import success
from login.forms import *
from login.models import Aspirante


# Create your views here.
def index(request):
    return render(request, 'aspirante/login_a.html')

def director(request):
    return render(request, 'director/login_d.html')


def registrar_a(request):
    return render(request, 'aspirante/registrar_a.html', {'form': RegistrarAspirante()})

def registrar_d(request):
    #muestra form de registro director
    return render(request, 'aspirante/registrar_d.html', {'form': RegistrarDirector()})

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

def guardar_d(request):
    #registrar director aquí
    pass
    return redirect('/aspirante/')

