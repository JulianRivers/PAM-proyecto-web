from django.urls import path
from .import views

urlpatterns = [
    path('director/form/<str:nombres>', views.head),
    path('director/')
]