from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.messages.api import success
from login.forms import *
from login.models import *
from werkzeug.security import generate_password_hash, check_password_hash
#verificar por correo aspirantes 
from django.core.mail import EmailMessage
#from django.conf import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
#from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token

# Create your views here.
def index(request):
    form = LoginAspirante()
    return render(request, 'aspirante/login_a.html', {'form':form})

def director(request):
    return render(request, 'director/login_d.html')

def registrar_a(request): 
    return render(request, 'aspirante/registrar_a.html', {'form': RegistrarAspirante()})

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
    auth_login(request, aspirante)
    return redirect('/aspirante/inicio/')

#login
def ingresar_a(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    usuario = Aspirante.objects.get(email=email)
    if usuario is not None and check_password_hash(usuario.password, password):
        auth_login(request, usuario)
        return redirect('/aspirante/inicio/')
    else:
        return redirect('/')

def recuperar_a(request):
    return render(request, 'aspirante/recuperar_a.html')