from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('director', views.director, name="director"),
    path('registrar', views.registrar_aspirante, name="registrar"),
    path('inicio', views.inicio, name="inicio"),
]
