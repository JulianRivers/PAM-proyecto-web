from django.contrib import admin
from django.urls import path
from . import views

app_name = 'director'
urlpatterns  = [
   path('director/inicio/', views.inicio),
   path('director/aspirantes/', views.aspirante),
]

