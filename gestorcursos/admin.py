from django.contrib import admin

from gestorcursos.models import Curso

# Register your models here.

# Se registra el modelo en el admin site de Django.
admin.site.register(Curso)