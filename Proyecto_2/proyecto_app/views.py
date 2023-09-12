from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'view/index.html')
def electronica(request):
    data = {"titulo" : "Electrónica"}
    return render(request, 'view/producto.html', data)
def juguetes(request):
    data = {"titulo" : "Juguetes"}
    return render(request, 'view/producto.html', data)
def ropa(request):
    data = {"titulo" : "Ropa"}
    return render(request, 'view/producto.html', data)