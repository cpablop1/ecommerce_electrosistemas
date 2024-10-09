from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def VistaEcommerce(request):
    return render(request, 'ecommerce/ecommerce.html')