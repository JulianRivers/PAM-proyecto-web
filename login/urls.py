from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registrar', views.registrar_aspirante)
]
