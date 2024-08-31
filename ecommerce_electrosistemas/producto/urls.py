from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaProducto, name='vista_producto'),
    path('categoria/', views.VistaCategoria, name='vista_categoria'),
    path('agregar-categoria/', views.AgregarCategoria, name='agregar_categoria'),
    path('listar-categorias/', views.ListarCategorias, name='listar_categorias'),
]
