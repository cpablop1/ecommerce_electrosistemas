from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

def VistaLogin(request):
    return render(request, 'login/login.html')

def IniciarSesion(request):
    if request.method == 'POST':
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username = user, password = password)
        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return JsonResponse({'msg': f'Bienvenido {user}, tienes privilegios de administrador.', 'res': True})
            else:
                return JsonResponse({'msg': 'No tienes permisos para acceder a esta área.', 'res': False})
        else:
            return JsonResponse({'msg': 'Ingrese una contraseña y usuario válido.', "res": False})

def CerrarSesion(request):
    logout(request)
    return redirect('vista_login')