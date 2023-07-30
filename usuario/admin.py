from django.contrib import admin

from usuario.models import Usuario

# Register your models here.

# Se registra el modelo en el admin site de Django.
admin.site.register(Usuario)