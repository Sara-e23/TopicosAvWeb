from django.contrib import admin
from .models import Carrera, Materia, Alumno, Inscripcion, Card

admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Alumno)
admin.site.register(Inscripcion)
admin.site.register(Card)  # Register the Card model

# Register your models here.
