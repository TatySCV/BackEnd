from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def empleadosview(request):
    emp = {
        'id' : 123,
        'nombre' : 'Juanito',
        'email' : 'juanito@gmail.com',
        'sueldo' : '1000000',
    }
    return JsonResponse(emp)