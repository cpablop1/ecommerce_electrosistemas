from django.contrib import admin

from .models import Productos, Categorias, Marcas

class MarcasAdmin (admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
    ]

class CategoriasAdmin (admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
    ]

    readonly_fields = ['id']

class ProductosAdmin (admin.ModelAdmin):
    list_display = [
        'id',
        'descripcion',
        'stock',
        'costo',
        'precio_publico',
        'precio_mayorista',
        'img_1',
        'img_2',
        'estante',
        'obtener_nombre_categoria',
        'obtener_nombre_marca',
        'id_usuario',
        'fecha_registro',
    ]
    readonly_fields = ['id']

    def obtener_nombre_categoria(self, obj):
        return obj.id_categoria.nombre  # Ajusta el campo según el nombre real en tu modelo relacionado
    obtener_nombre_categoria.admin_order_field = 'id_categoria'  # Permite ordenar por este campo
    obtener_nombre_categoria.short_description = 'Categoría'  # Nombre amigable en la tabla
    
    def obtener_nombre_marca(self, obj):
        return obj.id_marca.nombre  # Ajusta el campo según el nombre real en tu modelo relacionado
    obtener_nombre_marca.admin_order_field = 'id_marca'  # Permite ordenar por este campo
    obtener_nombre_marca.short_description = 'Marca'  # Nombre amigable en la tabla



admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Marcas, MarcasAdmin)
