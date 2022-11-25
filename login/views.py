from django.shortcuts import render, redirect
from django.contrib.messages.api import success
from login.forms import *
from general.models import *
from general.models import Aspirante
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.get(username=username)
        if usuario is not None and usuario.check_password(password):
            login(request, usuario)
            return redirect('/aspirante/inicio/')
    form = LoginAspirante()
    return render(request, 'aspirante/login_a.html', {'form': form})


def director(request):
    return render(request, 'director/login_d.html')

def registrar_a(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        foto = request.FILES.get('foto')
        email = request.POST['username']
        if request.POST.get('egresado_ufps', False) == "on":
            egresado_ufps = True
        else:
            egresado_ufps = False
        if request.POST.get('es_extranjero', False) == "on":
            es_extranjero = True
        else:
            es_extranjero = False
        form = RegistrarAspirante(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=email)
            username = form.cleaned_data['username']
            aspirante = Aspirante.objects.create(user_id=user.id, nombres=nombres, apellidos=apellidos, documento=documento,
                                                 email=email, egresado_ufps=egresado_ufps, es_extranjero=es_extranjero)
            login(request, user)
            return redirect('aspirante:inicio')
    else:
        form = RegistrarAspirante()
    context = {'form': form}
    return render(request, 'aspirante/registrar_a.html', context)


def recuperar_a(request):
    return render(request, 'aspirante/recuperacion_pass_a.html')

def prueba(request):
    return render(request, 'prueba.html')