from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'view/index.html')
def electronica(request):
    data = {"titulo" : "Electrónica", "foto1": "electronica1.jpg", "foto2": "electronica2.jpeg", "foto3": "electronica3.png", "producto1": "Computador", "producto2": "iPhone", "producto3": "Televisor"}
    return render(request, 'view/producto.html', data)
def juguetes(request):
    data = {"titulo" : "Juguetes", "foto1": "juguete1.jpg", "foto2": "juguete2.jpg", "foto3": "juguete3.jpg", "producto1": "Rompecabeza", "producto2": "Peluche", "producto3": "Camion"}
    return render(request, 'view/producto.html', data)
def ropa(request):
    data = {"titulo" : "Ropa", "foto1": "ropa1.jpg", "foto2": "ropa2.jpg", "foto3": "ropa3.jpg", "producto1": "Crop top", "producto2": "Jeans", "producto3": "Poleron"}
    return render(request, 'view/producto.html', data)