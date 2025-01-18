from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/modificar/<int:pk>/', views.modificar_alumno, name='modificar_alumno'),
    path('alumnos/eliminar/<int:pk>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('alumnos/buscar/', views.buscar_alumno, name='buscar_alumno'),
]