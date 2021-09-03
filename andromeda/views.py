from django.shortcuts import render, get_object_or_404
from .models import Banner, Producto, Galeria
# Create your views here.
 
def index(request):
    listaBanner = Banner.objects.order_by('titulo')[:3]
    listaProducto = Producto.objects.order_by('nombre')[:6]
    listaGaleria = Galeria.objects.order_by('nombre')
    context = {
        'listaBanner': listaBanner,
        'listaProducto': listaProducto,
        'listaGaleria': listaGaleria
    }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    return render(request, 'producto.html', {'producto': producto})