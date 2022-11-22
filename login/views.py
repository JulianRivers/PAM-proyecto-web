from django.shortcuts import render, redirect
from django.contrib.messages.api import success
from login.forms import *
from general.models import *
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from general.models import Aspirante
from django.contrib.auth.models import User
from django.contrib.auth import login

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

#verificar por correo aspirantes 
def send_action_email(Aspirante,request):
    current_site = get_current_site(request)
    email_subject = 'activa tu cuenta'
    email_body = render_to_string('authentication/activate.html',{
        'aspirante': Aspirante,
        'correo': current_site,
        'uid': urlsafe_base64_encode(force_bytes(Aspirante.pk)),
        'token': generate_token.make_token(Aspirante)
    })


def guardar_a(request):

    #verificar por correo aspirantes 
    send_action_email(Aspirante, request)

    #Registra Aspirantes
    nombres = request.POST['nombres']
    apellidos = request.POST['apellidos']
    documento = request.POST['documento']
    #foto = request.POST['foto'] #aún no
    email = request.POST['email']
    password = generate_password_hash(request.POST['password'], 'sha256', 30)
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



    #verificar por correo aspirantes 
    if not Aspirante.is_email_verified:
        messages.add_message(request, messages.ERROR, 'El correo no se ha verificado, revisa tu correo para verificarlo')
        return render(request, '/aspirante/')


    
    success(request, F"Bienvenido {nombres}")
    login(request, aspirante)
    return redirect('/aspirante/inicio/')

#login
def ingresar_a(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    usuario = Aspirante.objects.get(email=email)
    if usuario is not None and check_password_hash(usuario.password, password):
        auth_login(request, usuario)
        return redirect('/aspirante/inicio/')

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