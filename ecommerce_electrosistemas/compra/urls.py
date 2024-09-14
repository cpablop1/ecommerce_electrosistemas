from django.urls import path

from . import views

urlpatterns = [
    #path('', views.VistaProducto, name='vista_producto'),
    path('proveedor/', views.VistaProveedor, name='vista_proveedor'),
    path('agregar-proveedor/', views.AgregarProveedor, name='agregar_proveedor'),
]
