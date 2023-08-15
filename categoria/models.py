from django.db import models

# Create your models here.
class Categoria(models.Model):
    # no agregamos id porque django lo crea automaticamente
    categoria = models.CharField(max_length=50)
    estado = models.IntegerField('Estado', default=1)
    # OK

# Si quisieramos crear un nueva tabla en la base de datos que tenga algo que ver con categoria como subcategoria por ejemplo simplemente creamos el modelo dentro de esta misma aplicacion y no en su propia aplicacion
# class SubCategoria(models.Model):
    # no agregamos id porque django lo crea automaticamente
    # nombre = models.CharField(max_length=50)
    # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # relacion uno a muchos # ese on_delete es para que si se elimina una categoria se eliminen todas las subcategorias de esa categoria, recomiendo mejor usar models.SET_NULL para que no se eliminen las subcategorias de esa categoria, sino que se pongan en null
    # categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL)
    # estado = models.BooleanField('Estado', default=True)