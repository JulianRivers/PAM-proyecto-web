from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('aspirante/', views.index),
    path('director/', views.director),
    path('registrar_a/', views.registrar_a),
    path('guardar_a/', views.guardar_a),
    path('registrar_d/', views.registrar_d),
    path('guardar_d/', views.guardar_d),
]
