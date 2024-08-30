from django.shortcuts import render
from django.http import JsonResponse

def VistaProducto(request):
    return render(request, 'producto/producto.html')

def VistaCategoria(request):
    return render(request, 'categoria/categoria.html')

def AgregarCategoria(request):
    if request.method == 'POST':
        print('Creando categoria....')
    return JsonResponse({'res': True})