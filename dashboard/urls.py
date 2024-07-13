from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cargar_csv/', views.cargar_csv, name='cargar_csv'),
]
