from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaEcommerce, name='vista_ecommerce'),
    path('crear-usuario/', views.VistaCrearUsuario, name='vista_crear_usuario'),
    path('crear-usuario-cliente/', views.CrearUsuarioCliente, name='crear_usuario_cliente'),
    path('cerrar-sesion/', views.CerrarSesion, name='cerrar_sesion_cliente'),
    path('iniciar-sesion/', views.VistaIniciarSesion, name='vista_iniciar_sesion'),
    path('sesion/', views.IniciarSesion, name='iniciar_sesion'),
    path('carrito/', views.VistaCarrito, name='carrito'),
    path('perfil-usuario/', views.VistaPerfilUsuario, name='vista_perfil_usuario'),
    path('pedidos-usuario/', views.VistaPedidosUsuario, name='vista_pedidos_usuario'),
    path('perfil/', views.VistaPerfil, name='perfil'),
]
