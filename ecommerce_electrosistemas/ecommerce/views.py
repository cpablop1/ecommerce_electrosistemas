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
    id = request.GET.get('id', None)
    cliente = ''
    hay_cliente = False

    try:
        if id:
            cliente = Clientes.objects.get(id = id)
            hay_cliente = True
    except:
        cliente = ''
        hay_cliente = False
  
    return render(request, 'ecommerce/crear_usuario.html', {'cliente': cliente, 'hay_cliente': hay_cliente})

def VistaIniciarSesion(request):
    return render(request, 'ecommerce/iniciar_sesion.html')

def VistaCarrito(request):
    return render(request, 'ecommerce/carrito.html')

def VistaPerfilUsuario(request):
    try:
        cliente = UsuarioCliente.objects.get(id_usuario = request.user.id)
    except:
        cliente = ''
    return render(request, 'ecommerce/perfil_usuario.html', {'cliente': cliente})

def VistaPedidosUsuario(request):
    try:
        cliente = UsuarioCliente.objects.get(id_usuario = request.user.id)
    except:
        cliente = ''
    return render(request, 'ecommerce/pedidos_usuario.html', {'cliente': cliente})

def VistaPerfil(request):
    try:
        cliente = UsuarioCliente.objects.get(id_usuario = request.user.id)
    except:
        cliente = ''
    return render(request, 'ecommerce/perfil.html', {'cliente': cliente})

# Funcion para crear usuario para el cliente
def CrearUsuarioCliente(request):
    if request.method == 'POST': # Verificamos si se hizo una petición por POST
        # Recogemos los datos
        id = request.POST.get('id', None)
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

        # Validar id
        try:
            int(id)
        except:
            id = None

        # Variables de respuesta
        data = {}
        res = False
        crear = False
        msg = ''
        
        try:
            # Creamos el usuario
            if id is None:
                crear_usuario = User.objects.create_user(
                    username = usuario,
                    email = correo,
                    password = clave
                )
                crear_usuario.save()
            
            # Preparar los parametros por defecto del cliente
            defaults = {
                "nombres": nombres,
                "apellidos": apellidos,
                "nit": nit,
                "cui": cui,
                "empresa": empresa,
                "telefono": telefono,
                "direccion": direccion
            }

            if id is None:
                defaults['id_usuario'] = crear_usuario

            # Creamos el cliente
            crear_cliente = Clientes.objects.update_or_create(
                id = id,
                defaults = defaults
            )

            # Creamos Usuario cliente, para saber cual es el usuario del cliente
            if id is None:
                crear_usuario_cliente = UsuarioCliente.objects.create(
                    id_usuario = crear_usuario,
                    id_cliente = crear_cliente[0]
                )
                crear_usuario_cliente.save()
        
            res = True
            if crear_cliente[1]:
                msg = 'Usuario creada correctamente.'
                crear = True
            else:
                msg = 'Perfil actualizado correctamente.'

        except:
            res = False
            msg = 'Hubo un error al crear su usuario, recargue la página y vuelve a intentar.'
        
        data['res'] = res
        data['msg'] = msg
        data['crear'] = crear

    return JsonResponse(data)

def PerfilCliente(request):
    # Variables de respuesta
    res = False
    msg = ''
    data = {}
    data['data'] = []

    #try:
    # Buscar el del cliente mediante su usuario
    cliente = UsuarioCliente.objects.get(id_usuario = request.user.id).id_cliente

    # Prepar datos de respuesta
    data['data'].append(
        {
            'id': cliente.id,
            'nombres': cliente.nombres,
            'apellidos': cliente.apellidos,
            'nit': cliente.nit,
            'cui': cliente.cui,
            'empresa': cliente.empresa,
            'telefono': cliente.telefono,
            'direccion': cliente.direccion,
            'fecha_registro': cliente.fecha_registro,
        }
    )
    res = True
    msg = 'Perfil obtenido correctamente.'
    """ except:
        res = False
        msg = 'Hubo un error al ver perfil.' """

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