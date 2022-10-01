from itertools import product
from math import prod
from django.shortcuts import get_object_or_404, render
from .models import Categoria, Producto

# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    
    categoria_list = Categoria.objects.order_by('nombre')
    
    context = {
        'product_list' : product_list,
        'categoria_list' : categoria_list
    }
    return render(request, 'index.html', context)

def producto (request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    categoria_list = Categoria.objects.order_by('nombre')
    
    context = {
        'producto' : producto,
        'categoria_list' : categoria_list
    }
    
    return render(request, 'producto.html', context)
    
def categoria(request, categoria_id):
    categoria_list = Categoria.objects.order_by('nombre')
    
    producto = get_object_or_404(Producto, pk=categoria_id)
    
    productos = Producto.objects.order_by(pk=categoria_id)
    
    context = {
        'categoria_list' : categoria_list,
        'producto' : producto,
        'productos' : productos
    }
    return render(request, 'categoria.html', context)
