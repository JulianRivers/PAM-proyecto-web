from django.urls import path
from django.contrib.auth.views import LogoutView

from login.forms import LoginAspirante
from . import views

app_name="login"
urlpatterns = [
    path('',views.index, name='index'),
    path('aspirante/', views.index, name='aspirante'),
    path('login/', views.index, name='login'),
    path('director/', views.director, name='director'),
    path('registrar_a/', views.registrar_a, name='registrar_a'),
    path('recuperar_a/', views.recuperar_a, name='recuperar_a'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('prueba/', views.prueba)
]