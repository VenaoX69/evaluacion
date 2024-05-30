from django.shortcuts import render
from .models import Alumno

def alumno(request):
    inf_alum = Alumno.objects.all()
    return render(request, 'alumno.html', {'alumnos':inf_alum})