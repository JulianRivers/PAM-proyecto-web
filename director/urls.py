from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('director/inicio/', views.inicio)
]


urlpatterns = [
    path('director/form/<str:nombres>', views.head),
    path('director/')
]