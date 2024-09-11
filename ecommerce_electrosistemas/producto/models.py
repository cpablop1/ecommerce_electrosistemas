from django.db import models
from django.contrib.auth.models import User

import os

class Categorias(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.CharField(max_length = 300)

    def __str__(self) -> str:
        return self.nombre

class Marcas(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.CharField(max_length = 300)

    def __str__(self) -> str:
        return self.nombre

class Productos(models.Model):
    descripcion = models.CharField(max_length = 400, blank = False, null = False)
    stock = models.PositiveIntegerField(default = 0)
    costo = models.FloatField(default = 0)
    precio_publico = models.FloatField(default = 0)
    precio_mayorista = models.FloatField(default = 0)
    img_1 = models.ImageField(upload_to = 'producto', blank = True, null = True)
    img_2 = models.ImageField(upload_to = 'producto', blank = True, null = True)
    estante = models.CharField(max_length = 100)
    id_categoria = models.ForeignKey(Categorias, on_delete = models.CASCADE)
    id_marca = models.ForeignKey(Marcas, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        # Verificar si el objeto ya existe en la base de datos
        if self.pk:
            try:
                old_img_1 = Productos.objects.get(pk=self.pk).img_1
                old_img_2 = Productos.objects.get(pk=self.pk).img_2
                # Comparar si la imagen ha cambiado
                if old_img_1 and old_img_1 != self.img_1:
                    if os.path.isfile(old_img_1.path):
                        os.remove(old_img_1.path)  # Elimina la imagen anterior
                
                if old_img_2 and old_img_2 != self.img_2:
                    if os.path.isfile(old_img_2.path):
                        os.remove(old_img_2.path)  # Elimina la imagen anterior
                        
            except Productos.DoesNotExist:
                pass  # El objeto es nuevo, no hay imagen anterior

        super().save(*args, **kwargs)  # Guarda el objeto normalmente

class Descuentos(models.Model):
    fecha_inicio = models.DateField(blank = False, null = False)
    fecha_final = models.DateField(blank = False, null = False)
    porcentaje = models.FloatField(default = 0)
    estado = models.BooleanField(default = False)
    id_producto = models.ForeignKey(Productos, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add = True)