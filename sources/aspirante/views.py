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


def inscripcion_a(request):
    maestrias = Maestria.objects.all()
    if request.method == 'POST':
        inscripcion = Inscripcion()
        maestria = Maestria.objects.get(codigo=request.POST['id_maestria'])
        inscripcion.id_maestria = maestria
        user = request.user
        aspirante = Aspirante.objects.get(email=user.username)
        inscripcion.id_aspirante = aspirante
        inscripcion.foto = request.FILES.get('foto')
        inscripcion.copia_documento = request.FILES.get('copia_documento')
        inscripcion.diploma_pregrado = request.FILES.get('diploma_pregrado')
        inscripcion.notas_pregrado = request.FILES.get('notas_pregrado')
        inscripcion.comprobante_pago = request.FILES.get('comprobante_pago')
        inscripcion.resumen_cv = request.FILES.get('resumen_cv')
        inscripcion.referencia_uno = request.FILES.get('referencia_uno')
        inscripcion.referencia_dos = request.FILES.get('referencia_dos')
        inscripcion.formato_inscripcion = request.FILES.get(
            'formato_inscripcion')
        inscripcion.pasaporte_visa = request.FILES.get('pasaporte_visa')
        inscripcion.notas_apostilladas = request.FILES.get(
            'notas_apostilladas')
        inscripcion.diploma_apostillado = request.FILES.get(
            'diploma_apostillado')
        try:
            inscripcion.save()
            return redirect('login:index')
        except Exception as e:
            print(e)
    context = {'maestrias': maestrias}
    return render(request, 'aspirante/inscripcion_a.html', context)
