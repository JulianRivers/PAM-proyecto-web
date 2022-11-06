from django.shortcuts import render

# Create your views here.

def aspirante(request):
    return render(request,'dashboard-aspirante.html')
