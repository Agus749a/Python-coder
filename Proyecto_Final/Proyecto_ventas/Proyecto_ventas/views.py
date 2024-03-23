# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_ventas.models import Cliente
from app_ventas.models import Producto
from app_ventas.models import Pedido
# Create your views here.
def Agregar_clientes(request):
    if request.method == 'POST':
        zona = request.POST.get('zona')
        nombre = request.POST.get('nombre')
        calle = request.POST.get('calle')
        razon_social = request.POST.get('razon_social')
        numero_cel = request.POST.get('numero_cel')
        email = request.POST.get('email')
        cuit = request.POST.get('cuit')

        cliente_nuevo = Cliente(
            nombre=nombre,
            calle=calle,
            razon_social=razon_social,
            telefono= numero_cel,
            email=email,
            cuit=cuit,
            zona=zona
            )
        cliente_nuevo.save()

        return redirect('Agregar_clientes')

    return render(request, 'Agregar_clientes.html')

def Index(request):
    return render(request, 'Index.html')

def Agregar_productos(request):
    if request.method == 'POST':
        Nombre= request.POST.get('nombre')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        marca = request.POST.get('marca')
        tipo = request.POST.get('tipo')

        producto_nuevo = Producto(
            nombre=Nombre,
            stock=stock,
            precio=precio,
            marca=marca,
            tipo=tipo
        )
        producto_nuevo.save()

        return redirect('Agregar_productos')

    return render(request, 'Agregar_productos.html')

def ver_clientes(request):
   if request.method == 'GET':
        todos_clientes = Cliente.objects.all()

        zona = request.GET.get('zona')
        nombre = request.GET.get('nombre')
        calle = request.GET.get('calle')
        razon_social = request.GET.get('razon_social')
        numero_cel = request.GET.get('numero_cel')
        email = request.GET.get('email')
        cuit = request.GET.get('cuit')
        
        if nombre:
            todos_clientes = todos_clientes.filter(Nombre__icontains=nombre)
        elif cuit:
            todos_clientes = todos_clientes.filter(cuit__icontains=cuit)
        elif zona:
            todos_clientes = todos_clientes.filter(calle__icontains=zona)

        return render(request, 'Ver_clientes.html', {'clientes': todos_clientes})
