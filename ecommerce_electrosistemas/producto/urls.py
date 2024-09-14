from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaProducto, name='vista_producto'),
    path('categoria/', views.VistaCategoria, name='vista_categoria'),
    path('agregar-categoria/', views.AgregarCategoria, name='agregar_categoria'),
    path('listar-categorias/', views.ListarCategorias, name='listar_categorias'),
    path('ver-para-editar-categoria/', views.VerParaEditarCategoria, name='ver_para_editar_categoria'),
    path('marca/', views.VistaMarca, name='vista_marca'),
    path('agregar-marca/', views.AgregarMarca, name='agregar_marca'),
    path('listar-marcas/', views.ListarMarcas, name='listar_marcas'),
    path('ver-para-editar-marca/', views.VerParaEditarMarca, name='ver_para_editar_marca'),
    path('agregar-producto/', views.AgregarProducto, name='agregar_producto'),
    path('listar-productos/', views.ListarProductos, name='listar_productos'),
    path('ver-para-editar-producto', views.VerParaEditarProducto, name='ver_para_editar_producto'),
    path('descuento/', views.VistaDescuento, name='vista_descuento'),
    path('agregar-descuento/', views.AgregarDescuento, name='agregar_descuento'),
    path('listar-descuentos/', views.ListarDescuentos, name='listar_descuentos'),
    path('ver-para-editar-descuento/', views.VerParaEditarDescuento, name='ver_para_editar_descuento'),
]
