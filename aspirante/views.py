from django.shortcuts import render
from general.models import *
# Create your views here.

def inicio(request):
    user = request.user
    aspirante = Aspirante.objects.get(email=user.username)
    inscripcion = Inscripcion.objects.get(id_aspirante_id=aspirante.id)
    maestrias = Maestria.objects.all()

    context = {
        'aspirante': aspirante,
        'maestrias': maestrias,
    }
    return render(request,'aspirante/dashboard_a.html', context)
