from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaCliente, name='vista_cliente'),
    path('agregar-cliente/', views.AgregarCliente, name='agregar_cliente'),
    path('listar-clientes/', views.ListarClientes, name='listar_clientes'),
    path('ver-para-editar-cliente/', views.VerParaEditarCliente, name='ver_para_editar_cliente'),
    path('vista-venta/', views.VistaVenta, name='vista_venta'),
]
