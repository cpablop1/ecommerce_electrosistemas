from django.shortcuts import render
from django.http import JsonResponse

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
        id_compra = data.get('id_compra', None)
        id_proveedor = data.get('id_proveedor', None)
        _cantidad = data.get('cantidad', 1)
        # Formatear dato capturados por POST
        try:
            int(id_producto)
        except:
            id_producto = None

        try:
            int(id_compra)
        except:
            id_compra = None
        try:
            int(_cantidad)
        except:
            _cantidad = 1
        try:
            int(id_proveedor)
        except:
            id_proveedor = None
        # Variables de respuesta
        msg = ''
        res = False
        producto = None
        print('-------------------------------')
        print(id_proveedor)
        print('-------------------------------')
        # Obtenemos del producto
        try:
            producto = Productos.objects.get(id = id_producto)
        except:
            msg = 'Hay problemas al obtener el producto'
            res = False
        if id_compra is None:
            # Crear la compra
            compra = Compras.objects.update_or_create(
                id = id_compra,
                defaults = {
                    'subtotal': producto.costo,
                    'id_proveedor': Proveedores.objects.get(id = id_proveedor),
                    'id_usuario': User.objects.get(id = request.user.id)
                }
            )
            # Crear el detalle de compra
            detalle_compra = DetalleCompras.objects.create(
                cantidad = _cantidad,
                costo = producto.costo,
                total = producto.costo,
                id_producto = producto,
                id_compra = compra[0]
            )
            detalle_compra.save()

    return JsonResponse({'res': True})

def ListarDetalleCompras(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        compra = Compras.objects.filter(id_usuario = request.user.id)
        print('----------------------------')
        print(compra[0].id)
        print('----------------------------')
        detalle_compra = DetalleCompras.objects.filter(id_compra = compra[0].id)

        # Preparar el listado de categorías
        for dc in detalle_compra:
            data['data'].append({
                'id': dc.id,
                'cantidad': dc.cantidad,
                'costo': dc.costo,
                'total': dc.total,
                'id_producto': dc.id_producto.descripcion,
                'marca': dc.id_producto.id_marca.nombre,
                'precio_publico': dc.id_producto.precio_publico,
                'precio_mayorista': dc.id_producto.precio_mayorista,
                'id_compra': dc.id_compra.id,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)