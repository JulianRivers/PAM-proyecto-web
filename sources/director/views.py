from contextlib import _RedirectStream
from urllib import request
from django.core import serializers
from django.shortcuts import render
from general.models import Aspirante, Inscripcion

# Create your views here.
#Getting data from the HTML and accepting the POST request

def inicio(request):
    return render(request, 'director/dashboard_d.html')

def aspirante(request):
    aspirantes = Aspirante.objects.all()
    context = ({'aspirantes': aspirantes })
    return render(request, 'director/aspirantes.html', context)

def evaluar(request):
    inscripcion = Inscripcion.objects.all()
    context = ({'inscripciones': inscripcion})
    return render(request, 'director/evaluar_aspirante.html', context)

def horarios(request):
    return render(request, 'director/asignar_horarios.html')
