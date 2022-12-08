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
        try:
            usuario = User.objects.get(username=username)
            director = Director.objects.get(email= usuario.username)
            if usuario is not None and usuario.check_password(password):
                login(request, usuario)
                return redirect('/director/inicio/')
            else:
                messages.error(request, "Contraseña incorrecta")
                return redirect('login:director')
        except Exception as e:
            messages.error(request, "Su cuenta no está registrada como director")
            print(e)
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

def inscripcion_a(request):
    maestrias = Maestria.objects.all()
    if request.method == 'POST':
        inscripcion = Inscripcion()
        maestria = Maestria.objects.get(codigo=request.POST['id_maestria'])
        print(f"{maestria}")
        inscripcion.id_maestria = maestria
        user = request.user
        aspirante = Aspirante.objects.get(email=user.username)
        print(f"{aspirante}")
        inscripcion.id_aspirante = aspirante
        inscripcion.foto = request.FILES.get('foto')
        inscripcion.copia_documento = request.FILES.get('copia_documento')
        inscripcion.diploma_pregrado = request.FILES.get('diploma_pregrado')
        inscripcion.notas_pregrado = request.FILES.get('notas_pregrado')
        inscripcion.comprobante_pago = request.FILES.get('comprobante_pago')
        inscripcion.resumen_cv = request.FILES.get('resumen_cv')
        inscripcion.referencia_uno = request.FILES.get('referencia_uno')
        inscripcion.referencia_dos = request.FILES.get('referencia_dos')
        inscripcion.formato_inscripcion = request.FILES.get('formato_inscripcion')
        inscripcion.pasaporte_visa = request.FILES.get('pasaporte_visa')
        inscripcion.notas_apostilladas = request.FILES.get('notas_apostilladas')
        inscripcion.diploma_apostillado = request.FILES.get('diploma_apostillado')
        try:
            inscripcion.save()
            return redirect('login:index')
        except Exception as e:
            print(e)
    context = {'maestrias' : maestrias}
    return render(request, 'aspirante/inscripcion_a.html', context)
    
def prueba(request):
    return render(request, 'prueba.html')

def registrar_a(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        foto = request.FILES['foto']
        email = request.POST['username']
        if request.POST.get('egresado_ufps', False) == "on":
            egresado_ufps = True
        else:
            egresado_ufps = False
        if request.POST.get('es_extranjero', False) == "on":
            es_extranjero = True
        else:
            es_extranjero = False
        form = RegistrarAspirante(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=email)
            username = form.cleaned_data['username']
            aspirante = Aspirante.objects.create(user_id=user.id, nombres=nombres, apellidos=apellidos, documento=documento,
                                                 email=email, foto=foto, egresado_ufps=egresado_ufps, es_extranjero=es_extranjero)
            login(request, user)
            return redirect('aspirante:inicio')
    else:
        form = RegistrarAspirante()
    context = {'form': form}
    return render(request, 'aspirante/registrar_a.html', context)