from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaCliente, name='vista_cliente'),
    path('agregar-cliente/', views.AgregarCliente, name='agregar_cliente'),
    path('listar-clientes/', views.ListarClientes, name='listar_clientes'),
    path('ver-para-editar-cliente/', views.VerParaEditarCliente, name='ver_para_editar_cliente'),
    path('vista-venta/', views.VistaVenta, name='vista_venta'),
    path('agregar-venta/', views.AgregarVenta, name='agregar_venta'),
    path('listar-detalle-ventas/', views.ListarDetalleVentas, name='listar_detalle_ventas'),
    path('eliminar-venta/', views.EliminarVenta, name='eliminar_venta'),
    path('confirmar-venta/', views.ConfirmarVenta, name='confirmar_venta'),
    path('listar-ventas/', views.ListarVentas, name='listar_ventas'),
    path('listar-tipo-pagos/', views.ListarTipoPagos, name='listar_tipo_pagos'),
]
