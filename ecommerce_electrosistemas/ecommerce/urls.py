from django.urls import path

from . import views

urlpatterns = [
    path('', views.VistaEcommerce, name='vista_ecommerce'),
]
