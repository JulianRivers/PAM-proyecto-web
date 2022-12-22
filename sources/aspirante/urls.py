from django.urls import path
from . import views

app_name="aspirante"
urlpatterns = [
   path('aspirante/inicio/', views.inicio, name='inicio'),
   path('aspirante/inicio/<int:codigo>', views.maestria, name='maestria'),
   path('aspirante/inscripcion/', views.inscripcion_a, name='inscripcion'),
   path('aspirante/editar_info/', views.editar_info, name='editar_info')
]

