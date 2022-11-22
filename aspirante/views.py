from django.shortcuts import render
from general.models import Aspirante
# Create your views here.

def inicio(request):
    user = request.user
    aspirante = Aspirante.objects.get(email=user.username)
    context = {'aspirante': aspirante}
    return render(request,'aspirante/dashboard_a.html', context)
