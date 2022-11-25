from django.shortcuts import render, redirect
from general.models import *
# Create your views here.

def inicio(request):
    user = request.user
    aspirante = Aspirante.objects.get(email=user.username)
    #inscripcion = Inscripcion.objects.get(id_aspirante_id=aspirante.id)
    maestrias = Maestria.objects.all()
    context = {
    'aspirante': aspirante,
    'maestrias': maestrias,
    }
   
    return render(request,'aspirante/dashboard_a.html', context)

def maestria(request, codigo=115):
    user = request.user
    aspirante = Aspirante.objects.get(email=user.username)
    try:
       inscripcion = Inscripcion.objects.get(id_aspirante=aspirante.id)
       idMaestria = inscripcion.id_maestria_id
       
    except:
        inscripcion = None
        idMaestria = 0
        print("No está inscrito en esta maestria")
    
    maestria = Maestria.objects.get(codigo=codigo)
    context ={
        'maestria': maestria,
        'aspirante': aspirante,
        'inscripcion': inscripcion,
        'idMaestria': str(idMaestria),
        'codigo': str(codigo)
    }
    return render(request,'aspirante/maestria.html', context)
