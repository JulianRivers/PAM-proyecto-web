from django.urls import path
from . import views

app_name="aspirante"
urlpatterns = [
   path('aspirante/inicio/', views.inicio, name='inicio')
]

