from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaProducto, name='vista_producto'),
    #path('crear-producto/', views.CrearProducto, name='crear_producto'),
]
