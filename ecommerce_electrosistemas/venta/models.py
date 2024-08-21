from django.db import models
from django.contrib.auth.models import User
from producto.models import Productos

class Clientes(models.Model):
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    nit = models.CharField(max_length = 15)
    cui = models.CharField(max_length = 13)
    empresa = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 100)
    observaciones = models.TextField()
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

class Seguimientos(models.Model):
    nombre = models.CharField(max_length = 100)
    descricion = models.TextField()

class TipoPagos(models.Model):
    nombre = models.CharField(max_length = 100)
    descricion = models.TextField()

class Ventas(models.Model):
    subtotal = models.FloatField(default = 0)
    estado = models.BooleanField(default = False)
    id_seguimiento = models.ForeignKey(Seguimientos, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    id_tipo_pago = models.ForeignKey(TipoPagos, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

class DetalleVentas(models.Model):
    cantidad = models.PositiveIntegerField(default = 0)
    precio = models.FloatField(default = 0)
    total = models.FloatField(default = 0)
    id_producto = models.ForeignKey(Productos, on_delete = models.CASCADE)
    id_venta = models.ForeignKey(Ventas, on_delete = models.CASCADE)

class DetalleSeguimientos(models.Model):
    observaciones = models.TextField()
    id_seguimiento = models.ForeignKey(Seguimientos, on_delete = models.CASCADE)
    id_venta = models.ForeignKey(Ventas, on_delete = models.CASCADE)