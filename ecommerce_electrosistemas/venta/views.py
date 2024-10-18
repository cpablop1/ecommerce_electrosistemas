from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User

import json

from .models import Clientes, Ventas, DetalleVentas, Seguimientos, DetalleSeguimientos, TipoPagos
from producto.models import Productos
from ecommerce.models import UsuarioCliente

@staff_member_required(login_url='vista_login')
def VistaCliente(request):
    return render(request, 'cliente/cliente.html')

@staff_member_required(login_url='vista_login')
def VistaVenta(request):
    return render(request, 'venta/venta.html')

@staff_member_required(login_url='vista_login')
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

@staff_member_required(login_url='vista_login')
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

@staff_member_required(login_url='vista_login')
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
        id_tipo_pago = data.get('id_tipo_pago', None)
        buscar_cliente = ''
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
        
        try:
            int(id_tipo_pago)
        except:
            id_tipo_pago = None
        
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
        # Otenemos alguna venta activa (estado = false)
        try:
            venta = Ventas.objects.filter(id_usuario = request.user.id, estado = False)
        except:
            msg = 'Hay problemas con el proceso de la venta'
            res = False
        
        # Verificamos si existe algun cliente por parametro
        if id_cliente:
            id_cliente = Clientes.objects.get(id = id_cliente)
        else:
            buscar_cliente = UsuarioCliente.objects.get(id_usuario = request.user.id)
            if buscar_cliente:
                id_cliente = buscar_cliente.id_cliente
            else:
                id_cliente = Clientes.objects.get(id = 1)

        # Verificamos el tipo de pago
        if id_tipo_pago:
            id_tipo_pago = TipoPagos.objects.get(id = id_tipo_pago)
        else:
            id_tipo_pago = TipoPagos.objects.get(id = 1)

        if not venta:
    
            # Crear la venta
            crear_venta = Ventas.objects.create(
                subtotal = producto.precio_publico,
                id_seguimiento = Seguimientos.objects.get(id = 1),
                id_cliente = id_cliente,
                id_usuario = User.objects.get(id = request.user.id),
                id_tipo_pago = id_tipo_pago
            )
            #crear_compra.save()
            
            # Crear el detalle de venta
            DetalleVentas.objects.create(
                cantidad = 1,
                precio = producto.precio_publico,
                total = producto.precio_publico,
                id_producto = producto,
                id_venta = crear_venta
            )

            # Crear seguimiento de pedido
            DetalleSeguimientos.objects.create(
                id_seguimiento = crear_venta.id_seguimiento,
                id_venta = crear_venta
            )
            
            #detalle_compra.save()
            if buscar_cliente:
                msg = 'Producto agregado al carrito.'
            else:    
                msg = 'Venta creada correctamente.'
            
            res = True
    
        else:
            # Primero buscamos si existe el producto en el detalle de compra
            detalle_venta = DetalleVentas.objects.filter(id_producto = producto.id, id_venta = venta[0].id)
           
            if not detalle_venta: # Si no existe el producto en el detalle
                # Creamos un detalle de compra
                DetalleVentas.objects.create(
                    cantidad = 1,
                    precio = producto.precio_publico,
                    total = producto.precio_publico,
                    id_producto = producto,
                    id_venta = venta[0]
                )
                # Y luego actualizamos el subtotal de la compra general
                venta[0].subtotal = sum(item.total for item in DetalleVentas.objects.filter(id_venta = venta[0].id))
                venta[0].id_cliente = id_cliente
                venta[0].save()

                msg = 'Producto agregado al carrito.'
                res = True
            else: # En caso contrario solo actualizamos ese detalle
                try:
                    # Actualizamos la cantidad del detalle de venta
                    if _cantidad is None:
                        detalle_venta[0].cantidad += 1
                    else:
                        detalle_venta[0].cantidad = int(_cantidad)
                    # Actualizamos el total del detalle de compra
                    detalle_venta[0].total = int(detalle_venta[0].cantidad) * int(detalle_venta[0].precio)
                    # Guaradamos los cambios
                    detalle_venta[0].save()
                    # Actualizamos el subtotal de la venta general
                    venta[0].subtotal = sum(item.total for item in DetalleVentas.objects.filter(id_venta = venta[0].id))
                    venta[0].id_cliente = id_cliente
                    venta[0].save()

                    msg = 'Carrito alctualizado, vaya a la carrito para ver detalles.'
                    res = True
                except:
                    msg = 'Hubo un error a actualizar el detalle de la venta.'
                    print('Hubo un error a actualizar el detalle de la venta.')
                    res = False

        data['res'] = res
        data['msg'] = msg

    return JsonResponse(data)

@login_required(login_url='vista_login')
def ConfirmarVenta(request):
    if request.method == 'POST':
        data = json.loads(request.body) # Parseamos el cuerpo de la solicitad a formato JSON
        id_venta = data.get('id_venta', None) # Buscamos el id de la venta
        id_tipo_pago = data.get('id_tipo_pago', None) # Buscamos el id del tipo de pago

        # Verificar si el id es valido
        try:
            int(id_venta)
        except:
            id_venta = None

        # Obtenemos la venta
        venta = Ventas.objects.get(id = id_venta)

        if not venta.estado: # El estado es False
            # Obtemos los detalles de la venta
            detalle_venta = DetalleVentas.objects.filter(id_venta = venta.id)
            
            # Descontamos los productos del stock
            for item in detalle_venta:
                item.id_producto.stock -= item.cantidad
                item.id_producto.save()
            # Y luego cambiamos el estado del pedido a True para indicar que se ha confirmado
            venta.estado = True
            if id_tipo_pago:
                venta.id_tipo_pago = TipoPagos.objects.get(id = id_tipo_pago)
            venta.save()

    return JsonResponse({'res': True})

@login_required(login_url='vista_login')
def ListarDetalleVentas(request):
    id = request.GET.get('id', None)

    try:
        int(id)
    except:
        id = None
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        if id:
            detalle_venta = DetalleVentas.objects.filter(id_venta = id)
            data['subtotal'] = sum(item.total for item in detalle_venta)
        else:
            venta = Ventas.objects.filter(id_usuario = request.user.id, estado = False)
            data['subtotal'] = venta[0].subtotal
            data['id_cliente'] = venta[0].id_cliente.id
            data['direccion_cliente'] = venta[0].id_cliente.direccion
            data['telefono_cliente'] = venta[0].id_cliente.telefono
            data['id_venta'] = venta[0].id
            
            detalle_venta = DetalleVentas.objects.filter(id_venta = venta[0].id).order_by('id')

        # Preparar el listado de detalle de compra
        for dv in detalle_venta:
            data['data'].append({
                'id': dv.id,
                'cantidad': dv.cantidad,
                'precio': dv.precio,
                'total': dv.total,
                'producto': dv.id_producto.descripcion,
                'id_producto': dv.id_producto.id,
                'img': dv.id_producto.img_1.name,
                'marca': dv.id_producto.id_marca.nombre,
                'precio': dv.precio
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def EliminarVenta(request):
    if request.method == 'POST':
        data = json.loads(request.body) # Parseamos el cuerpo de la solicitad a formato JSON
        id_detalle_venta = data.get('id_detalle_venta', None) # Buscamos el id del detalle de venta
        id_venta = data.get('id_venta', None) # Buscamos si quiere eliminar todo

        # Datos de respuestas
        res = False
        msg = ''

        # Verificar si el es valido
        try:
            int(id_detalle_venta)
        except:
            id_detalle_venta = None
        
        try:
            id_venta = int(id_venta)
        except:
            id_venta = None

        if id_venta:
            try:
                venta = Ventas.objects.get(id = id_venta)
                venta.delete()

                res = True
                msg = 'Venta eliminada correctamente.'
            except:
                res = False
                msg = 'Hubo un error al eliminar la venta.'
        elif id_detalle_venta:
            dv = DetalleVentas.objects.get(id = id_detalle_venta)
            ventas = DetalleVentas.objects.filter(id_venta = dv.id_venta)
           
            try:
                if len(ventas) == 1: # Si solo hay un detalle de venta, eleminamos la venta completa
                    dv.id_venta.delete()
                else:
                    # Eliminamos el detalle de venta
                    dv.delete()
                    # Actulizamos el subtotal de la venta general
                    dv.id_venta.subtotal = sum(item.total for item in DetalleVentas.objects.filter(id_venta = dv.id_venta))
                    dv.id_venta.save()

                res = True
                msg = 'Elemento eliminado correctamente.'
            except:
                res = False
                msg = 'Hubo un error al eliminar el elemento.'

    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarVentas(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []
    # Instanciar el cliente
    cliente = UsuarioCliente.objects.filter(id_usuario = request.user.id)

    try:
        # Instanciar el modelo
        if cliente:
            ventas = Ventas.objects.filter(id_usuario = request.user.id).order_by('id')
        else:
            ventas = Ventas.objects.filter().order_by('id')
    
        # Preparar el listado de detalle de venta
        for ven in ventas:
            data['data'].append({
                'id': ven.id,
                'estado': ven.estado,
                'seguimiento': ven.id_seguimiento.nombre,
                'id_seguimiento': ven.id_seguimiento.id,
                'cliente': f'{ven.id_cliente.nombres} {ven.id_cliente.apellidos} {(ven.id_cliente.empresa if len(ven.id_cliente.empresa) != 0 else "")}',
                'tipo_pago': ven.id_tipo_pago.nombre,
                'subtotal': ven.subtotal,
                'usuario': ven.id_usuario.username,
                'fecha': ven.fecha_registro,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def ListarTipoPagos(request):
    # Inicializar variables de respuestas
    data = {}
    data['data'] = []
    res = False
    msg = ''

    try:
        # Instancia modelo de TipoPago
        tipo_pago = TipoPagos.objects.all()

        # Estructurar datos datos de respuestas
        for tp in tipo_pago:
            data['data'].append(
                {
                    'id': tp.id,
                    'nombre': tp.nombre,
                    'descricion': tp.descricion
                }
            )
            res = True
    except:
        res = False
        msg = 'Hubo un error a listar los tipos de pago.'

    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)

@login_required(login_url='vista_login')
def ListarDetalleSeguimiento(request):
    # Capturamos los datos de entrada
    id_venta = request.GET.get('id_venta', None)

    # Preparando variales de respuesta
    res = False
    msg = ''
    data = {}
    data['data'] = []

    # Instanciamos el modelo
    seguimientos = DetalleSeguimientos.objects.filter(id_venta = id_venta)

    for ds in seguimientos:
        data['data'].append(
            {
                'observaciones': ds.observaciones,
                'seguimiento': ds.id_seguimiento.nombre,
                'descripcion': ds.id_seguimiento.descricion,
                'fecha': ds.fecha_registro
            }
        )
    
    return JsonResponse(data)

@login_required(login_url='vista_login')
def ListarSeguimientos(request):
    # Instanciamos el modelo
    seguimientos = Seguimientos.objects.all()
    # >Preparamos variables de respuesta
    res = False
    msg = ''
    data = {}
    data['data'] = []

    # >Estructuramos datos de respuesta
    for s in seguimientos:
        data['data'].append(
            {
                'id': s.id,
                'nombre': s.nombre,
                'descripcion': s.descricion
            }
        )

    return JsonResponse(data)

@staff_member_required(login_url='vista_login')
def CrearDetalleSeguimiento(request):
    # Capturando los dato de entrada
    id_seguimiento = request.GET.get('id_seguimiento', None)
    id_venta = request.GET.get('id_venta', None)

    # Formateamos los datos de entrada y reasignamos
    try:
        int(id_seguimiento)
        id_seguimiento = Seguimientos.objects.get(id = id_seguimiento)
    except:
        id_seguimiento = None

    try:
        int(id_venta)
        id_venta = Ventas.objects.get(id = id_venta)
    except:
        id_venta = None

    # > Estableciendo los variables de respuesta
    res = False
    msg = ''
    data = {}

    try:
        # Crear seguimiento de pedido
        DetalleSeguimientos.objects.create(
            id_seguimiento = id_seguimiento,
            id_venta = id_venta
        )
        # Y actualizamos el estado del seguimiento
        id_venta.id_seguimiento = id_seguimiento
        id_venta.save()
        res = True
        msg = 'Pedido actualizado correctamente.'
    except:
        res = False
        msg = 'Hubo un problema al actualizar pedido.'
    
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)