from django.shortcuts import render

# Create your views here.
def plantilla(request):
    return render(request, 'plantilla_app/plantilla.html')
def info(request):
    data={"id":"123", "nombre":"Tatiana Campos", "email":"hola@hola.com"}
    return render(request, 'plantilla_app/info.html', data)