from contextlib import _RedirectStream
from urllib import request
from django.core import serializers
from django.shortcuts import render
from general.models import Aspirante

# Create your views here.
#Getting data from the HTML and accepting the POST request

def inicio(request):
    return render(request, 'director/inicio.html')

def aspirante(request):
    
    aspirantes = Aspirante.objects.all()
    context = ({'aspirantes': aspirantes })
    return render(request, 'director/admitidos_d.html', context)
