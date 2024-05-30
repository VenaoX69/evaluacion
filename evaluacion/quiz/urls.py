from django.urls import path
from .views import alumno

urlpatterns = [
    path('alumnos/', alumno, name="alumnos")
]