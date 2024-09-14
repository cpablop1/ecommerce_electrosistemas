from django.shortcuts import render
from django.http import JsonResponse

from .models import Proveedores
from django.contrib.auth.models import User

def VistaProveedor(request):
    return render(request, 'proveedor/proveedor.html')

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