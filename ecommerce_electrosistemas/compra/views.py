from django.shortcuts import render
from django.http import JsonResponse

from .models import Proveedores
from django.contrib.auth.models import User

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