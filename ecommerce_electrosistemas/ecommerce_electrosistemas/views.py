from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='vista_login')
def VistaPlantillaPrincipal(request):
    return render(request, 'plantilla_principal/plantilla_principal.html')