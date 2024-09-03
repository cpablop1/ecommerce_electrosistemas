from django.shortcuts import render
from django.http import JsonResponse

from .models import Categorias

def VistaProducto(request):
    return render(request, 'producto/producto.html')

def VistaCategoria(request):
    return render(request, 'categoria/categoria.html')

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