from django.db import models
from django.contrib.auth.models import User
from venta.models import Clientes

class UsuarioCliente(models.Model):
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)