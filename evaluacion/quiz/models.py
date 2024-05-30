from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    ficha = models.CharField(max_length=70)
    edad = models.IntegerField()
    
    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'
        
    def __str__(self):
        return self.nombre