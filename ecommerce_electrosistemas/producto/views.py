from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Categorias, Marcas, Productos, Descuentos
from django.contrib.auth.models import User

import json

@login_required(login_url='vista_login')
def VistaProducto(request):
    return render(request, 'producto/producto.html')

@login_required(login_url='vista_login')
def VistaCategoria(request):
    return render(request, 'categoria/categoria.html')

@login_required(login_url='vista_login')
def VistaMarca(request):
    return render(request, 'marca/marca.html')

@login_required(login_url='vista_login')
def VistaDescuento(request):
    return render(request, 'descuento/descuento.html')

@login_required(login_url='vista_login')
def AgregarCategoria(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        nombre = request.POST.get('nombre', '').upper()
        descripcion = request.POST.get('descripcion', '').upper()

        # Formateamos el id
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la categoría.'
            id = None

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Categoria
        categoria = Categorias.objects.update_or_create(
            id = id,
            defaults = {
                "nombre": nombre,
                "descripcion": descripcion
            }
        )

        # Revisamos si es un nuevo registro o una actualización
        if categoria[1]:
            res = True
            msg = 'Categoría creada correctamente.'
        else:
            res = True
            msg = 'Categoría actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarCategorias(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        categorias = Categorias.objects.all()

        # Preparar el listado de categorías
        for cat in categorias:
            data['data'].append({
                'id': cat.id,
                'nombre': cat.nombre,
                'descripcion': cat.descripcion
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def VerParaEditarCategoria(request):
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
        msg = 'Hubo un error al visualizar la categoría.'

    # Comprobamos si es válido el id
    if flag:
        categoria = Categorias.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar la categoría.'
        
    data['data'] = {
        'id': categoria.id,
        'nombre': categoria.nombre,
        'descripcion': categoria.descripcion
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)


@login_required(login_url='vista_login')
def AgregarMarca(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        nombre = request.POST.get('nombre', '').upper()
        descripcion = request.POST.get('descripcion', '').upper()

        # Formateamos el id
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la categoría.'
            id = None

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Categoria
        marca = Marcas.objects.update_or_create(
            id = id,
            defaults = {
                "nombre": nombre,
                "descripcion": descripcion
            }
        )

        # Revisamos si es un nuevo registro o una actualización
        if marca[1]:
            res = True
            msg = 'Marca creada correctamente.'
        else:
            res = True
            msg = 'Marca actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarMarcas(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        marcas = Marcas.objects.all()

        # Preparar el listado de categorías
        for mar in marcas:
            data['data'].append({
                'id': mar.id,
                'nombre': mar.nombre,
                'descripcion': mar.descripcion
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def VerParaEditarMarca(request):
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
        msg = 'Hubo un error al visualizar la marca.'

    # Comprobamos si es válido el id
    if flag:
        marca = Marcas.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar la marca.'
        
    data['data'] = {
        'id': marca.id,
        'nombre': marca.nombre,
        'descripcion': marca.descripcion
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)

@login_required(login_url='vista_login')
def AgregarProducto(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        descripcion = request.POST.get('descripcion', '').upper()
        costo = request.POST.get('costo', 0)
        precio_publico = request.POST.get('precio_publico', 0)
        precio_mayorista = request.POST.get('precio_mayorista', 0)
        img_1 = request.FILES.get('img_1', None)
        img_2 = request.FILES.get('img_2', None)
        estante = request.POST.get('estante', '').upper()
        id_categoria = request.POST.get('id_categoria', None)
        id_marca = request.POST.get('id_marca', None)

        check_img_1 = request.POST.get('check_img_1')
        check_img_2 = request.POST.get('check_img_2')

        print('-----------------')
        print(f'check_img_1 {type(check_img_1)}')
        print(f'check_img_2 {type(check_img_2)}')
        print('-----------------')

        # Formateamos los datos obtenidos
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la categoría.'
            id = None
        
        try:
            int(id_categoria)
        except:
            id_categoria = None
        
        try:
            int(id_marca)
        except:
            id_marca = None
        
        try:
            float(precio_publico)
        except:
            precio_publico = 0
        
        try:
            float(precio_mayorista)
        except:
            precio_mayorista = 0

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Producto
        data = {
            "descripcion": descripcion,
            "costo": costo,
            "precio_publico": precio_publico,
            "precio_mayorista": precio_mayorista,
            "estante": estante,
            "id_categoria": Categorias.objects.get(id = id_categoria),
            "id_marca": Marcas.objects.get(id = id_marca),
        }
        if img_1 != None:
            data['img_1'] = img_1

        if img_2 != None:
            data['img_2'] = img_2

        if check_img_1 != None and id != None:
            data['img_1'] = ''
        
        if check_img_2 != None and id != None:
            data['img_2'] = ''


        if id == None:
            data['id_usuario'] = User.objects.get(id = request.user.id)

        producto = Productos.objects.update_or_create(
            id = id,
            defaults = data
        )

        # Revisamos si es un nuevo registro o una actualización
        if producto[1]:
            res = True
            msg = 'Producto creada correctamente.'
        else:
            res = True
            msg = 'Producto actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarProductos(request):
    id = request.GET.get('id', None)
    try:
        int(id)
    except:
        id = None

    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        if id != None:
            # Instanciar el modelo
            productos = Productos.objects.get(id = id)
            # Preparar el listado de productos
            print(productos.descripcion)
            print('ñasjdflkñsajfkdljdj')
            data['data'] = [{
                    'id': productos.id,
                    'descripcion': productos.descripcion,
                    'stock': productos.stock,
                    'costo': productos.costo,
                    'precio_publico': productos.precio_publico,
                    'precio_mayorista': productos.precio_mayorista,
                    'img_1': productos.img_1.name,
                    'img_2': productos.img_2.name,
                    'estante': productos.estante,
                    'categoria': productos.id_categoria.nombre,
                    'marca': productos.id_marca.nombre,
                    'usuario': productos.id_usuario.username,
                    'fecha_registro': productos.fecha_registro,
                }]
        else:
            # Instanciar el modelo
            productos = Productos.objects.all()
            # Preparar el listado de productos
            for pro in productos:
                data['data'].append({
                    'id': pro.id,
                    'descripcion': pro.descripcion,
                    'stock': pro.stock,
                    'costo': pro.costo,
                    'precio_publico': pro.precio_publico,
                    'precio_mayorista': pro.precio_mayorista,
                    'img_1': pro.img_1.name,
                    'img_2': pro.img_2.name,
                    'estante': pro.estante,
                    'categoria': pro.id_categoria.nombre,
                    'marca': pro.id_marca.nombre,
                    'usuario': pro.id_usuario.username,
                    'fecha_registro': pro.fecha_registro,
                })

        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def VerParaEditarProducto(request):
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
        msg = 'Hubo un error al visualizar la producto.'

    # Comprobamos si es válido el id
    if flag:
        producto = Productos.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar la producto.'
        
    data['data'] = {
        'id': producto.id,
        'descripcion': producto.descripcion,
        'costo': producto.costo,
        'precio_publico': producto.precio_publico,
        'precio_mayorista': producto.precio_mayorista,
        'img_1': producto.img_1.name,
        'img_2': producto.img_2.name,
        'estante': producto.estante,
        'id_categoria': producto.id_categoria.id,
        'id_marca': producto.id_marca.id,
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)

@login_required(login_url='vista_login')
def AgregarDescuento(request):
    if request.method == 'POST':
        # Recoger los datos por POST
        id = request.POST.get('id', None)
        fecha_inicio = request.POST.get('fecha_inicio', '')
        fecha_final = request.POST.get('fecha_final', '')
        porcentaje = request.POST.get('porcentaje', 0)
        id_producto = request.POST.get('id_producto', None)

        # Formateamos el id
        try:
            int(id)
        except:
            msg = 'Hubo un error al visualizar la descuento.'
            id = None

        # Inicializando las respuestas del servidor
        res = False
        msg = ''
        
        # Creamos o actulizamos la el objecto Descuento
        descuento = Descuentos.objects.update_or_create(
            id = id,
            defaults = {
                "fecha_inicio": fecha_inicio,
                "fecha_final": fecha_final,
                "porcentaje": porcentaje,
                "id_producto": Productos.objects.get(id = id_producto),
                "id_usuario": User.objects.get(id = request.user.id),
            }
        )

        # Revisamos si es un nuevo registro o una actualización
        if descuento[1]:
            res = True
            msg = 'Descuento creada correctamente.'
        else:
            res = True
            msg = 'Descuento actualizada correctamente.'
    
    # Y finalmente devolvemos una respuesta
    return JsonResponse({'res': res, 'msg': msg})

@login_required(login_url='vista_login')
def ListarDescuentos(request):
    # Inicializamos variables de respuesta
    data = {}
    data['data'] = []

    try:
        # Instanciar el modelo
        descuentos = Descuentos.objects.all()

        # Preparar el listado de descuentos
        for des in descuentos:
            data['data'].append({
                'id': des.id,
                'fecha_inicio': des.fecha_inicio,
                'fecha_final': des.fecha_final,
                'porcentaje': des.porcentaje,
                'producto': des.id_producto.descripcion,
                'usuario': des.id_usuario.username,
                'estado': des.estado,
                'fecha_registro': des.fecha_registro,
            })
        
        data['res'] = True
    except:
        data['res'] = False

    return JsonResponse(data)

@login_required(login_url='vista_login')
def VerParaEditarDescuento(request):
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
        msg = 'Hubo un error al visualizar la descuento.'

    # Comprobamos si es válido el id
    if flag:
        descuento = Descuentos.objects.get(id = id)
    else:
        msg = 'Hubo un error al visualizar la descuento.'
        
    data['data'] = {
        'id': descuento.id,
        'fecha_inicio': descuento.fecha_inicio,
        'fecha_final': descuento.fecha_final,
        'estado': descuento.estado,
        'porcentaje': descuento.porcentaje,
        'id_producto': descuento.id_producto.id
    }
    data['res'] = res
    data['msg'] = msg

    return JsonResponse(data)