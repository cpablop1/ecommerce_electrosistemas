from django.shortcuts import render
from django.http import JsonResponse

from django.db import IntegrityError, transaction

from .models import Proveedores, Compras, DetalleCompras
from producto.models import Productos
from django.contrib.auth.models import User

import json

def VistaProveedor(request):
    return render(request, 'proveedor/proveedor.html')

def VistaCompra(request):
    return render(request, 'compra/compra.html')

def AgregarProveedor(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        nombres = request.POST.get('nombres', '').upper()
        apellidos = request.POST.get('apellidos', '').upper()
        nit = request.POST.get('nit', '').upper()
        dpi = request.POST.get('dpi', '').upper()
        empresa = request.POST.get('empresa', '').upper()
        telefono = request.POST.get('telefono', '').upper()
        direccion = request.POST.get('direccion', '').upper()
        observaciones = request.POST.get('observaciones', '').upper()

        # Formateamos el id
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la proveedor.'
            id = None

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Categoria
        proveedor = Proveedores.objects.update_or_create(
            id = id,
            defaults = {
                "nombres": nombres,
                'apellidos': apellidos,
                'nit': nit,
                'dpi': dpi,
                'empresa': empresa,
                'telefono': telefono,
                'direccion': direccion,
                'observaciones': observaciones,
                'id_usuario': User.objects.get(id = request.user.id)
            }
        )

        # Revisamos si es un nuevo registro o una actualización
        if proveedor[1]:
            res = True
            msg = 'Proveedor creada correctamente.'
        else:
            res = True
            msg = 'Proveedor actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

def ListarProveedores(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        proveedores = Proveedores.objects.all()

        # Preparar el listado de categorías
        for pro in proveedores:
            data['data'].append({
                'id': pro.id,
                'nombres': pro.nombres,
                'apellidos': pro.apellidos,
                'nit': pro.nit,
                'dpi': pro.dpi,
                'empresa': pro.empresa,
                'telefono': pro.telefono,
                'direccion': pro.direccion,
                'observaciones': pro.observaciones,
                'usuario': pro.id_usuario.username,
                'fecha_registro': pro.fecha_registro,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

def VerParaEditarProveedor(request):
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
        msg = 'Hubo un error al visualizar el proveedor.'

    # Comprobamos si es válido el id
    if flag:
        proveedor = Proveedores.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar el proveedor.'
        
    data['data'] = {
        'id': proveedor.id,
        'nombres': proveedor.nombres,
        'apellidos': proveedor.apellidos,
        'nit': proveedor.nit,
        'dpi': proveedor.dpi,
        'empresa': proveedor.empresa,
        'telefono': proveedor.telefono,
        'direccion': proveedor.direccion,
        'observaciones': proveedor.observaciones,
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)

def AgregarCompra(request):
    if request.method == 'POST':
        # Deserializar el cuerpo de la solicitud JSON
        data = json.loads(request.body)
        id_producto = data.get('id_producto', None)
        # id_compra = data.get('id_compra', None)
        id_proveedor = data.get('id_proveedor', None)
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
            int(id_proveedor)
        except:
            id_proveedor = None
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
            compra = Compras.objects.filter(id_usuario = request.user.id, estado = False)
        except:
            msg = 'Hay problemas con el proceso de la compra'
            res = False

        if not compra:
            #try:
            # Crear la compra
            crear_compra = Compras.objects.create(
                subtotal = producto.costo,
                id_proveedor =  Proveedores.objects.get(id = id_proveedor),
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

def ConfirmarCompra(request):
    if request.method == 'POST':
        data = json.loads(request.body) # Parseamos el cuerpo de la solicitad a formato JSON
        id_compra = data.get('id_compra', None) # Buscamos el id de la compra

        # Verificar si el es valido
        try:
            int(id_compra)
        except:
            id_compra = None

        compra = Compras.objects.get(id = id_compra)
        if not compra.estado:
            detalle_compra = DetalleCompras.objects.filter(id_compra = compra.id)
            print(compra)
            for item in detalle_compra:
                item.id_producto.stock += item.cantidad
                item.id_producto.save()
            
            compra.estado = True
            compra.save()

    return JsonResponse({'res': True})


def ListarDetalleCompras(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        compra = Compras.objects.filter(id_usuario = request.user.id, estado = False)
        data['subtotal'] = compra[0].subtotal
        data['id_proveedor'] = compra[0].id_proveedor.id
        data['id_compra'] = compra[0].id
        
        detalle_compra = DetalleCompras.objects.filter(id_compra = compra[0].id).order_by('id')

        # Preparar el listado de detalle de compra
        for dc in detalle_compra:
            data['data'].append({
                'id': dc.id,
                'cantidad': dc.cantidad,
                'costo': dc.costo,
                'total': dc.total,
                'producto': dc.id_producto.descripcion,
                'id_producto': dc.id_producto.id,
                'marca': dc.id_producto.id_marca.nombre,
                'precio_publico': dc.id_producto.precio_publico,
                'precio_mayorista': dc.id_producto.precio_mayorista,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)