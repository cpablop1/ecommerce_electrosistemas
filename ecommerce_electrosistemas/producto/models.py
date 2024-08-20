from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.CharField(max_length = 300)

class Marcas(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.CharField(max_length = 300)

class Productos(models.Model):
    descripcion = models.CharField(max_length = 400, blank = False, null = False)
    stock = models.PositiveIntegerField(default = 0)
    costo = models.FloatField(default = 0)
    precio_publico = models.FloatField(default = 0)
    precio_mayorista = models.FloatField(default = 0)
    img_1 = models.ImageField(upload_to = 'img_productos', blank = True, null = True)
    img_2 = models.ImageField(upload_to = 'img_productos', blank = True, null = True)
    estante = models.CharField(max_length = 100)
    id_categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

class Descuentos(models.Model):
    fecha_inicio = models.DateField(blank = False, null = False)
    fecha_final = models.DateField(blank = False, null = False)
    porcentaje = models.FloatField(default = 0)
    estado = models.BooleanField(default = False)
    id_producto = models.ForeignKey(Productos, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)