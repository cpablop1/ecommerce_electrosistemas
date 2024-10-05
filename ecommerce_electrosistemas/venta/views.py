from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

import json

from .models import Clientes, Ventas, DetalleVentas, DetalleSeguimientos
from producto.models import Productos

@login_required(login_url='vista_login')
def VistaCliente(request):
    return render(request, 'cliente/cliente.html')

@login_required(login_url='vista_login')
def VistaVenta(request):
    return render(request, 'venta/venta.html')

@login_required(login_url='vista_login')
def AgregarCliente(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        nombres = request.POST.get('nombres', '').upper()
        apellidos = request.POST.get('apellidos', '').upper()
        nit = request.POST.get('nit', '').upper()
        cui = request.POST.get('cui', '').upper()
        empresa = request.POST.get('empresa', '').upper()
        telefono = request.POST.get('telefono', '').upper()
        direccion = request.POST.get('direccion', '').upper()
        observaciones = request.POST.get('observaciones', '').upper()

        # Formateamos el id
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la cliente.'
            id = None

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Categoria
        cliente = Clientes.objects.update_or_create(
            id = id,
            defaults = {
                "nombres": nombres,
                'apellidos': apellidos,
                'nit': nit,
                'cui': cui,
                'empresa': empresa,
                'telefono': telefono,
                'direccion': direccion,
                'observaciones': observaciones,
                'id_usuario': User.objects.get(id = request.user.id)
            }
        )

        # Revisamos si es un nuevo registro o una actualización
        if cliente[1]:
            res = True
            msg = 'Cliente creada correctamente.'
        else:
            res = True
            msg = 'Cliente actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarClientes(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        clientes = Clientes.objects.all()

        # Preparar el listado de categorías
        for cli in clientes:
            data['data'].append({
                'id': cli.id,
                'nombres': cli.nombres,
                'apellidos': cli.apellidos,
                'nit': cli.nit,
                'cui': cli.cui,
                'empresa': cli.empresa,
                'telefono': cli.telefono,
                'direccion': cli.direccion,
                'observaciones': cli.observaciones,
                'usuario': cli.id_usuario.username,
                'fecha_registro': cli.fecha_registro,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def VerParaEditarCliente(request):
    # Capturamos el id por get
    id = request.GET.get('id', None)
    # Variables de inicializacion y de respuesta
    flag = False
    res = False
    msg = ''
    data = {}
    # Formateamos el id
    try:
        int(id)
        flag = True
    except:
        msg = 'Hubo un error al visualizar el cliente.'

    # Comprobamos si es válido el id
    if flag:
        cliente = Clientes.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar el cliente.'
        
    data['data'] = {
        'id': cliente.id,
        'nombres': cliente.nombres,
        'apellidos': cliente.apellidos,
        'nit': cliente.nit,
        'cui': cliente.cui,
        'empresa': cliente.empresa,
        'telefono': cliente.telefono,
        'direccion': cliente.direccion,
        'observaciones': cliente.observaciones,
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)

@login_required(login_url='vista_login')
def AgregarVenta(request):
    if request.method == 'POST':
        # Deserializar el cuerpo de la solicitud JSON
        data = json.loads(request.body)
        id_producto = data.get('id_producto', None)
        # id_compra = data.get('id_compra', None)
        id_cliente = data.get('id_cliente', None)
        _cantidad = data.get('cantidad', None)
        # Formatear dato capturados por POST
        try:
            int(id_producto)
        except:
            id_producto = None
        try:
            int(_cantidad)
        except:
            _cantidad = None
        try:
            int(id_cliente)
        except:
            id_cliente = None
        # Variables de respuesta
        msg = ''
        res = False
        producto = None
        data = {}
        # Obtenemos del producto
        try:
            producto = Productos.objects.get(id = id_producto)
        except:
            msg = 'Hay problemas al obtener el producto'
            res = False
        # Otenemos alguna compra activa (estado = false)
        try:
            venta = Ventas.objects.filter(id_usuario = request.user.id, estado = False)
        except:
            msg = 'Hay problemas con el proceso de la venta'
            res = False

        if not venta:
            #try:
            # Crear la compra
            crear_venta = Ventas.objects.create(
                subtotal = producto.precio_publico,
                id_cliente =  Proveedores.objects.get(id = id_proveedor),
                id_usuario = User.objects.get(id = request.user.id)
            )
            #crear_compra.save()
            # Crear el detalle de compra
            DetalleCompras.objects.create(
                cantidad = 1,
                costo = producto.costo,
                total = producto.costo,
                id_producto = producto,
                id_compra = crear_compra
            )
            #detalle_compra.save()
            msg = 'Compra creada correctamente.'
            res = True
    
        else:
            # Primero buscamos si existe el producto en el detalle de compra
            detalle_compra = DetalleCompras.objects.filter(id_producto = producto.id, id_compra = compra[0].id)
           
            if not detalle_compra: # Si no existe el producto en el detalle
                # Creamos un detalle de compra
                DetalleCompras.objects.create(
                    cantidad = 1,
                    costo = producto.costo,
                    total = producto.costo,
                    id_producto = producto,
                    id_compra = compra[0]
                )
                # Y luego actualizamos el subtotal de la compra general
                compra[0].subtotal = sum(item.total for item in DetalleCompras.objects.filter(id_compra = compra[0].id))
                compra[0].id_proveedor = Proveedores.objects.get(id = id_proveedor)
                compra[0].save()

                res = True
            else: # En caso contrario solo actualizamos ese detalle
                try:
                    # Actualizamos la cantidad del detalle de compra
                    if _cantidad is None:
                        detalle_compra[0].cantidad += 1
                    else:
                        detalle_compra[0].cantidad = int(_cantidad)
                    # Actualizamos el total del detalle de compra
                    detalle_compra[0].total = int(detalle_compra[0].cantidad) * int(detalle_compra[0].costo)
                    # Guaradamos los cambios
                    detalle_compra[0].save()
                    # Actualizamos el subtotal de la compra general
                    compra[0].subtotal = sum(item.total for item in DetalleCompras.objects.filter(id_compra = compra[0].id))
                    compra[0].id_proveedor = Proveedores.objects.get(id = id_proveedor)
                    compra[0].save()
        
                    res = True
                except:
                    msg = 'Hubo un error a actualizar el detalle de la compra.'
                    print('Hubo un error a actualizar el detalle de la compra.')
                    res = False

        data['res'] = res
        data['msg'] = msg

    return JsonResponse(data)