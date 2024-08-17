from django.shortcuts import render

def VistaProducto(request):
    return render(request, 'producto/producto.html')