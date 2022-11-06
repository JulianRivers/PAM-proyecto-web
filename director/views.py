from django.http import HttpResponse
# Create your views here.

def head(request, nombres):
    print(nombres)
    return HttpResponse("<h1>PANEL DE DIRECTOR</h1>")
