from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from apps.modelo.models import Estudiante, Materia
from .forms import FormularioEstudiante, FormularioMateria
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User   


def index(request):
    usuario = request.user
    if usuario.groups.filter(name = "gestion_estudiantes").exists():
        listaEstudiantes = Estudiante.objects.all() 
        #manejo del ORM 
        
        return render (request, 'estudiantes/index.html', locals())

def crearEstudiante(request):
    formulario_estudiante = FormularioEstudiante(request.POST)
    formulario_materia = FormularioMateria(request.POST)
    if request.method == 'POST':
        if formulario_estudiante.is_valid() 

            estudiante = Estudiante()
            datos_estudiante = formulario_estudiante.cleaned_data
            estudiante.cedula = datos_estudiante.get('cedula')
            estudiante.nombres = datos_estudiante.get('nombres')
            estudiante.apellidos = datos_estudiante.get('apellidos')
            #ORM
            
            Estudiante.save()

        return redirect(index)
    return render (request, 'estudiantes/crear.html', locals())



def listarMaterias(request, cedula):
    estudiante = Estudiante.objects.get(cedula=cedula)
    materia = Materia.objects.filter(estudiante=estudiante)
    return render(request, 'materias/index.html', locals())

def crearMaterias(request):
    formulario_materia = FormularioMateria(request.POST)
    estudiante = Estudiante.objects.get(cedula=cedula)
    if request.method == 'POST':
        if formulario_materia.is_valid():
            materia = Materia()
            datos_materia = formulario_materia.cleaned_data
            materia.nombre = datos_materia.get('nombre')
            materia.nota1 = datos_materia.get('nota1')
            materia.nota2 = datos_materia.get('nota2')
            materia.nota3 = datos_materia.get('nota3')
            materia.promedio = datos_materia.get('promedio')
            
            materia.estudiante = estudiante
            #ORM
            materia.save()
        return redirect(index)
    return render (request, 'materias/crear.html', locals())
