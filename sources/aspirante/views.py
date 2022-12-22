from django.shortcuts import render, redirect
from django.contrib import messages
from general.models import *
from aspirante.forms import *

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
    # inscripcion = Inscripcion.objects.get(id_aspirante_id=aspirante.id)
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
    user = request.user
    aspirante = Aspirante.objects.get(email=user.username)
    maestrias = Maestria.objects.all()
    if request.method == 'POST':
        i = Inscripcion()
        maestria = Maestria.objects.get(codigo=request.POST['id_maestria'])
        i.id_maestria = maestria
        i.id_aspirante = aspirante
        i.foto = request.FILES.get('foto')
        i.copia_documento = request.FILES.get('copia_documento')
        i.diploma_pregrado = request.FILES.get('diploma_pregrado')
        i.notas_pregrado = request.FILES.get('notas_pregrado')
        i.comprobante_pago = request.FILES.get('comprobante_pago')
        i.resumen_cv = request.FILES.get('resumen_cv')
        i.referencia_uno = request.FILES.get('referencia_uno')
        i.referencia_dos = request.FILES.get('referencia_dos')
        i.formato_inscripcion = request.FILES.get('formato_inscripcion')
        i.pasaporte_visa = request.FILES.get('pasaporte_visa')
        i.notas_apostilladas = request.FILES.get('notas_apostilladas')
        i.diploma_apostillado = request.FILES.get('diploma_apostillado')
        try:
            i.save()
            messages.success(request, "Felicitaciones! te has inscrito con éxito")
            return redirect("aspirante:inscripcion")
        except Exception as e:
            messages.error(request, "No ha iniciado sesión")
            return redirect("login:index")
    context = {
        'user': user,
        'aspirante': aspirante,
        'maestrias': maestrias
    }
    return render(request, 'aspirante/inscripcion.html', context)

def editar_info(request):
    user = request.user
    email = user.username
    aspirante = Aspirante.objects.get(email=email)
    context = {
        'aspirante' : aspirante
    }
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        foto = request.FILES.get('foto')
        
        if nombres:
            Aspirante.objects.filter(email=email).update(nombres=nombres)
        if apellidos:
            Aspirante.objects.filter(email=email).update(apellidos=apellidos)
        if documento:
            Aspirante.objects.filter(email=email).update(documento=documento)
        if foto:
            Aspirante.objects.filter(email=email).update(foto=foto)
        else:
            return redirect("aspirante:editar_info")
    return render(request, 'aspirante/editar_informacion.html', context)
