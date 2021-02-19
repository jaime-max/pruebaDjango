from django import forms
from apps.modelo.models import Estudiante, Materia

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["cedula","nombres","genero","apellidos"]

class FormularioMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre","nota1","nota2","nota3","promedio"]