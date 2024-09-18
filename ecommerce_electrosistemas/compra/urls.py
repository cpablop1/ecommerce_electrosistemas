from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaCompra, name='vista_compra'),
    path('proveedor/', views.VistaProveedor, name='vista_proveedor'),
    path('agregar-proveedor/', views.AgregarProveedor, name='agregar_proveedor'),
    path('listar-proveedores/', views.ListarProveedores, name='listar_proveedores'),
    path('ver-para-editar-proveedor/', views.VerParaEditarProveedor, name='ver_para_editar_proveedor'),
    path('agregar-compra/', views.AgregarCompra, name='agregar_compra'),
]
