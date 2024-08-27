from django.shortcuts import render

def VistaPlantillaPrincipal(request):
    return render(request, 'plantilla_principal/plantilla_principal.html')