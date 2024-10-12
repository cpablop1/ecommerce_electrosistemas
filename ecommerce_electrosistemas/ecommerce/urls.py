from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaEcommerce, name='vista_ecommerce'),
    path('crear-usuario/', views.VistaCrearUsuario, name='vista_crear_usuario'),
]
