from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from venta.models import Clientes
from .models import UsuarioCliente

def VistaEcommerce(request):
    return render(request, 'ecommerce/ecommerce.html')

def VistaCrearUsuario(request):
    return render(request, 'ecommerce/crear_usuario.html')

def VistaIniciarSesion(request):
    return render(request, 'ecommerce/iniciar_sesion.html')

def VistaCarrito(request):
    return render(request, 'ecommerce/carrito.html')

def VistaPerfilUsuario(request):
    return render(request, 'ecommerce/perfil_usuario.html')

def VistaPedidosUsuario(request):
    return render(request, 'ecommerce/pedidos_usuario.html')

def VistaPerfil(request):
    return render(request, 'ecommerce/perfil.html')

# Funcion para crear usuario para el cliente
def CrearUsuarioCliente(request):
    if request.method == 'POST': # Verificamos si se hizo una petición por POST
        # Recogemos los datos
        nombres = request.POST.get('nombres', '').upper()
        apellidos = request.POST.get('apellidos', '').upper()
        nit = request.POST.get('nit', '').upper()
        cui = request.POST.get('cui', '').upper()
        empresa = request.POST.get('empresa', '').upper()
        telefono = request.POST.get('telefono', '').upper()
        direccion = request.POST.get('direccion', '').upper()
        """ ---------------------------------------------------- """
        usuario = request.POST.get('usuario', '')
        correo = request.POST.get('correo', '')
        clave = request.POST.get('clave', '')

        # Variables de respuesta
        data = {}
        res = False
        msg = ''
        
        try:
            # Creamos el usuario
            crear_usuario = User.objects.create_user(
                username = usuario,
                email = correo,
                password = clave
            )
            crear_usuario.save()
            
            # Creamos el cliente
            crear_cliente = Clientes.objects.create(
                nombres = nombres,
                apellidos = apellidos,
                nit = nit,
                cui = cui,
                empresa = empresa,
                telefono = telefono,
                direccion = direccion,
                id_usuario = crear_usuario
            )
            crear_cliente.save()

            # Creamos Usuario cliente, para saber cual es el usuario del cliente
            crear_usuario_cliente = UsuarioCliente.objects.create(
                id_usuario = crear_usuario,
                id_cliente = crear_cliente
            )
            crear_usuario_cliente.save()
            
            res = True
            msg = 'Usuario creada correctamente.'
        except:
            res = False
            msg = 'Hubo un error al crear su usuario, recargue la página y vuelve a intentar.'
        
        data['res'] = res
        data['msg'] = msg

    return JsonResponse(data)

# Funcion para cerrar sesión
def CerrarSesion(request):
    logout(request)
    return redirect('vista_ecommerce')

# Funcion para iniciar sesión
def IniciarSesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario', '')
        clave = request.POST.get('clave', '')

        user = authenticate(request, username = usuario, password = clave)
        if user is not None:
            login(request, user)
            return JsonResponse({'msg': f'Bienvenido {user}', 'res': True})
        else:
            return JsonResponse({'msg': 'Ingrese una contraseña y usuario válido.', "res": False})