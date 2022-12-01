from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name="login"
urlpatterns = [
    path('',views.index, name='index'),
    path('aspirante/', views.index, name='aspirante'),
    path('login/', views.index, name='login'),
    path('director/', views.director, name='director'),
    path('registrar_a/', views.registrar_a, name='registrar_a'),
    path('recuperar_a/', views.recuperar_a, name='recuperar_a'),
    path('aspirante/logout/', LogoutView.as_view(template_name='aspirante/logout_a.html'), name='logout_a'),
    path('director/logout/', LogoutView.as_view(template_name='director/logout_d.html'), name='logout_'),
    path('prueba/', views.prueba)
]
