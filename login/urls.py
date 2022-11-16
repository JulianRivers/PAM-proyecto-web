from django.urls import path
from django.contrib.auth import login
from . import views

urlpatterns = [
    path('',views.index),
    path('aspirante/', views.index),
    path('director/', views.director),
    path('registrar_a/', views.registrar_a),
    path('guardar_a/', views.guardar_a),
    path('ingresar_a/', views.ingresar_a),
]
