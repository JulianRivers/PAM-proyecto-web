from django.shortcuts import render, redirect
from login.forms import *
from general.models import *
from general.models import Aspirante
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.db import transaction


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            usuario = User.objects.get(username=username)
            if usuario is not None and usuario.check_password(password):
                login(request, usuario)
                return redirect('aspirante:inicio')
            else:
                messages.error(request, "Contraseña incorrecta")
        except Exception as e:
            messages.error(
                request, "Lo sentimos, no pudimos encontrar tu cuenta")
            usuario = None
            print(e)
    form = Login()
    return render(request, 'aspirante/login_a.html', {'form': form})


def director(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.get(username=username)
        if usuario is not None and usuario.check_password(password):
            login(request, usuario)
            return redirect('/director/inicio/')
    context = {'form': Login()}
    return render(request, 'director/login_d.html', context)


@transaction.atomic
def registrar_a(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        foto = request.FILES['foto']
        email = request.POST['username']
        egresado_ufps = request.POST.get('egresado_ufps', False) == "on"
        es_extranjero = request.POST.get('es_extranjero', False) == "on"
        form = RegistrarAspirante(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=email)
            try:
                Aspirante.objects.create(user_id=user.id, nombres=nombres, apellidos=apellidos, documento=documento,
                                         email=email, foto=foto, egresado_ufps=egresado_ufps, es_extranjero=es_extranjero)
                login(request, user)
                messages.success(request, f"Bienvenido {nombres}")
            except Exception as e:
                print(e)
                messages.error(request, f"Ya existe un usuario registrado con este documento.")
                return redirect('login:registrar_a')
            return redirect('aspirante:inicio')
        else:
            messages.error(
                request, "Ya existe un usuario registrado con este correo.")
    else:
        form = RegistrarAspirante()
    context = {'form': form}
    return render(request, 'aspirante/registrar_a.html', context)


def recuperar_a(request):
    return render(request, 'aspirante/recuperacion_pass_a.html')

def registrar_d(request):
    pass

def prueba(request):
    return render(request, 'prueba.html')
