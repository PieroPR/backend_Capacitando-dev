from django.db import models
from categoria.models import Categoria
from usuario.models import Usuario

# Create your models here.

class Curso(models.Model):
    # No agregamos id porque django lo crea automaticamente
    titulo = models.CharField(max_length=250)
    # portada = models.ImageField(upload_to='cursos', null=True, blank=True)
    portada = models.CharField(max_length=90)
    url_video_intro = models.CharField(max_length=90)
    url_portada_det = models.CharField(max_length=90)
    hora_duracion = models.IntegerField() # creo que seria mejor un decimal porque a veces duran horas y media como 1.5 o 2.5 horas
    total_clases = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # relacion uno a muchos # ese on_delete es para que si se elimina una categoria se eliminen todos los cursos de esa categoria, recomiendo mejor usar models.SET_NULL para que no se eliminen los cursos de esa categoria, sino que se pongan en null
    # categoria = models.ForeignKey(categoria, on_delete=models.SET_NULL)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    estado = models.IntegerField('Estado', default=1) # recomendaria cambiar el nombre de estado a activo acá y en los demas modelos porque es mas entendible (si está activo es True y si está inactivo es False)
    created_at = models.DateTimeField(auto_now_add=True) # se agrega la fecha automaticamente cuando se crea el registro
    updated_at = models.DateTimeField(auto_now=True) # se agrega la fecha automaticamente cuando se actualiza el registro
    # OK


# Creo esta clase dentro de la aplicacion curso y no en su propia aplicacion porque al ser una tabla relacional no tiene sentido crearle una aplicacion propia
class CursoUsuario(models.Model):
    # No agregamos id porque django lo crea automaticamente
    # id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # relacion uno a muchos # ese on_delete es para que si se elimina un curso se eliminen todos los estudiantes de ese curso, recomiendo mejor usar models.SET_NULL para que no se eliminen los estudiantes de ese curso, sino que se pongan en null
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    # OK

class Sesion(models.Model):
    # no agregamos id porque django lo crea automaticamente
    nombre_sesion = models.CharField(max_length=90)
    descripcion = models.TextField()
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    estado = models.IntegerField('Estado', default=1)
    # OK

class Curso_Temas(models.Model):
    # no agregamos id porque django lo crea automaticamente
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    temas = models.TextField()
    estado = models.IntegerField('Estado', default=1)
    # OK


class Contenido(models.Model):
    # no agregamos id porque django lo crea automaticamente
    id_seccion = models.ForeignKey(Sesion, on_delete=models.SET_NULL, null=True)
    titulo = models.TextField()
    descripcion = models.TextField()
    url_video = models.CharField(max_length=300)
    minutos_video = models.CharField(max_length=20)
    estado = models.IntegerField('Estado', default=1)
    # OK

class Recurso(models.Model):
    # no agregamos id porque django lo crea automaticamente
    id_contenido = models.ForeignKey(Contenido, on_delete=models.SET_NULL, null=True)
    nombre = models.TextField()
    tipo_recurso = models.CharField(max_length=45)
    url = models.CharField(max_length=45)
    archivo = models.CharField(max_length=80)
    estado = models.IntegerField('Estado', default=1)
    # OK

class contenido_vistas(models.Model):
    # no agregamos id porque django lo crea automaticamente
    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    id_contenido = models.ForeignKey(Contenido, on_delete=models.SET_NULL, null=True)
    min_video = models.CharField(max_length=5)
    # OK

class Requisitos(models.Model):
    # no agregamos id porque django lo crea automaticamente
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    requisitos = models.TextField()
    estado = models.IntegerField('Estado', default=1)
    # models.IntegerField
    # OK