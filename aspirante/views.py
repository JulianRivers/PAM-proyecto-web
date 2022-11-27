from django.shortcuts import render, redirect
from django.contrib import messages
from general.models import *

# Create your views here.


def inicio(request):
    user = request.user
    try:
        aspirante = Aspirante.objects.get(email=user.username)
        maestrias = Maestria.objects.all()
        context = {
            'user': user,
            'aspirante': aspirante,
            'maestrias': maestrias,
        }
    except Exception as e:
        print(e)
        messages.error(request, "No ha iniciado sesión")
        return redirect('login:index')
    #inscripcion = Inscripcion.objects.get(id_aspirante_id=aspirante.id)
    return render(request, 'aspirante/dashboard_a.html', context)


def maestria(request, codigo=115):
    user = request.user
    try:
        aspirante = Aspirante.objects.get(email=user.username)
        try:
            inscripcion = Inscripcion.objects.get(id_aspirante=aspirante.id)
            idMaestria = inscripcion.id_maestria_id
        except Exception as e:
            inscripcion = None
            idMaestria = 0
            print(e)
            print("por aqui")
        maestria = Maestria.objects.get(codigo=codigo)
        context = {
            'maestria': maestria,
            'aspirante': aspirante,
            'inscripcion': inscripcion,
            'idMaestria': str(idMaestria),
            'codigo': str(codigo),
        }
    except Exception as e:
        messages.error(request, "No ha iniciado sesión")
        return redirect("login:index")
    return render(request, 'aspirante/maestria.html', context)