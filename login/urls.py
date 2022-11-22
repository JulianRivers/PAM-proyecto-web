from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name="login"
urlpatterns = [
    path('',views.index, name='index'),
    path('aspirante/', views.index, name='aspirante'),
    path('director/', views.director, name='director'),
    path('registrar_a/', views.registrar_a, name='registrar_a'),
    path('recuperar_a/', views.recuperar_a, name='recuperar_a'),
    path('login/', LoginView.as_view(template_name='aspirante/login_a.html'), name='login')
]
