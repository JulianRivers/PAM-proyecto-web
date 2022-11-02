from django.shortcuts import render

from login.forms import RegistrarAspirante

# Create your views here.
def index(request):
    return render(request, 'loginDirector.html')

def registrar_aspirante(request):
    return render(request, 'registrarse.html', {'form':RegistrarAspirante()})