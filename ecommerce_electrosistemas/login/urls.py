from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaLogin, name='vista_login'),
    path('iniciar-sesion/', views.IniciarSesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.CerrarSesion, name='cerrar_sesion'),
]
