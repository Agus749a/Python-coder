from django.shortcuts import render, redirect
from django.http import HttpResponse
from Felfort_retail.models import clientes
from Felfort_retail.models import productos
from Felfort_retail.models import Pedido
from Felfort_retail.models import PedidoProducto
# Create your views here.
def Generar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calle = request.POST.get('calle')
        razon_social = request.POST.get('razon_social')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        cuit = request.POST.get('cuit')

        cliente_nuevo = clientes(
            Nombre=nombre,
            calle=calle,
            razon_social=razon_social,
            telefono=telefono,
            email=email,
            cuit=cuit
        )
        cliente_nuevo.save()

        return redirect('Generar_cliente')

    return render(request, 'Generar_cliente.html')

def index(request):
    return render(request, 'index.html')

def venta(request):
    productos_vendidos = []
    total_venta = 0
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))

        producto = productos.objects.get(id_producto=producto_id)
        subtotal = producto.Precio * cantidad
        total_venta += subtotal
        
        productos_vendidos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        if 'finalizar_venta' in request.POST:
            return render(request, 'detalle_venta.html', {
                'productos_vendidos': productos_vendidos,
                'total_venta': total_venta
            })

    return render(request, 'buscar_cliente.html')

def agregar_producto(request):
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        Product_name = request.POST.get('Product_name')
        stock = request.POST.get('stock')
        Product_descripcion = request.POST.get('Product_descripcion')
        Precio = request.POST.get('Precio')

        producto_nuevo = productos(
            id_producto=id_producto,
            Product_name=Product_name,
            stock=stock,
            Product_descripcion=Product_descripcion,
            Precio=Precio
        )
        producto_nuevo.save()

        return redirect('agregar_producto')

    return render(request, 'agregar_producto.html')

def ver_clientes(request):
   if request.method == 'GET':
        todos_clientes = clientes.objects.all()

        nombre = request.GET.get('nombre')
        cuit = request.GET.get('cuit')
        calle = request.GET.get('calle')
        
        if nombre:
            todos_clientes = todos_clientes.filter(Nombre__icontains=nombre)
        elif cuit:
            todos_clientes = todos_clientes.filter(cuit__icontains=cuit)
        elif calle:
            todos_clientes = todos_clientes.filter(calle__icontains=calle)

        return render(request, 'Clientes.html', {'clientes': todos_clientes})