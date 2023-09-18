from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor, Curso

# Create your views here.
"""
def profe_nuevo(request):
    profeNu = Profesor(nombre = "Ciro", Apellido = "leon", email="ciroleon@hotmail.com", profesion="fisico" )
    profeNu.save()
    
    return HttpResponse(f"hemos guardado al profe{profeNu.nombre}")
"""

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_curso(request):
    return render(request, "AppCoder/ver_curso.html")

def ver_profesor(request):
    return render(request, "AppCoder/ver_profes.html") 

def ver_entregas(request):
    return render(request, "AppCoder/ver_entrega.html")  

def ver_estudiantes(request):
    return render(request, "AppCoder/ver_estudiante.html")