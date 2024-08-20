from django.db import models
from django.contrib.auth.models import User
from producto.models import Productos

class Proveedores(models.Model):
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    nit = models.CharField(max_length = 15)
    dpi = models.CharField(max_length = 13)
    empresa = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 100)
    observaciones = models.TextField()
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

class Compras(models.Model):
    subtotal = models.FloatField(default = 0)
    estado = models.BooleanField(default = False)
    id_proveedor = models.ForeignKey(Proveedores, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)


class DetalleCompras(models.Model):
    cantidad = models.PositiveIntegerField(default = 0)
    costo = models.FloatField(default = 0)
    total = models.FloatField(default = 0)
    id_producto = models.ForeignKey(Productos, on_delete = models.CASCADE)
    id_compra = models.ForeignKey(Compras, on_delete = models.CASCADE)