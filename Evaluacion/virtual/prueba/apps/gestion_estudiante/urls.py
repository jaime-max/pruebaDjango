from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='estudiantes'),
    path('crearEstudiantes', views.crearEstudiante, name='crear_estudiantes'),

    path('materias/<int:cedula>/', views.listarMaterias, name="materias"),
    path('crearMaterias/<int:cedula>/', views.crearMaterias, name='crear_materias'),
]