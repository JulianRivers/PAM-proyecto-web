from django.shortcuts import render, redirect
from login.forms import *
from general.models import *
from general.models import Aspirante
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = User.objects.get(username=username)
        if usuario is not None and usuario.check_password(password):
            login(request, usuario)
            return redirect('/aspirante/inicio/')
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
