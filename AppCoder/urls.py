from django.urls import path

from AppCoder.views import * 

urlpatterns = [
    
    path('inicio/', inicio, name="inicio"),
    path('cursos/', ver_curso, name="Cursos"),
    path('profesores/', ver_profesor, name="Profesor"),
    path('estudiantes/', ver_estudiantes, name="Estudiantes"),
    path('entregables/', ver_entregas, name="Entregables"),
    
    
]

    