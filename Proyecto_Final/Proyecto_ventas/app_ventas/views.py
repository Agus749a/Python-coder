# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_ventas.models import Cliente
from app_ventas.models import Producto
from app_ventas.models import Pedido
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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
            numero_cel=numero_cel,
            email=email,
            cuit=cuit,
            zona=zona
            )
        cliente_nuevo.save()

        return redirect('Agregar_clientes')

    return render(request, 'Agregar_clientes.html')

def Index(request):
    return render(request, 'Index.html', {"mensaje": "Bienvenido"})

@login_required
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
            todos_clientes = todos_clientes.filter(nombre__icontains=nombre)
        elif cuit:
            todos_clientes = todos_clientes.filter(cuit__icontains=cuit)
        elif zona:
            todos_clientes = todos_clientes.filter(zona__icontains=zona)

        return render(request, 'Ver_clientes.html', {'clientes': todos_clientes})

@login_required
def Cargar_venta(request):
    if request.method=='POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        Total=request.POST.get('Total')
        Entregado=request.POST.get('Entregado')

        Nuevo_pedido = Pedido(
            nombre_cliente=nombre_cliente,
            Total=Total,
            Entregado=Entregado
        )
        Nuevo_pedido.save()
    
        return redirect ('Cargar_venta')

    return render (request, 'Cargar_venta.html')

@login_required
def Ver_pedidos (request):
    if request.method == 'GET':
        todos_pedidos = Pedido.objects.all()

        nombre_cliente = request.GET.get('nombre_cliente')
        id_factura = request.GET.get('id_factura')
        Total = request.GET.get('Total')
        Entregado = request.GET.get('Entregado')
        
        
        if id_factura:
            todos_pedidos = todos_pedidos.filter(id_factura__icontains=id_factura)

        return render(request, 'Ver_pedidos.html', {'pedidos': todos_pedidos})

@login_required
def actualizar_pedido(request, id):
    pedido = Pedido.objects.get(id_factura=id)
    
    if request.method == 'POST':

        pedido.nombre_cliente = request.POST.get('nombre_cliente')
        pedido.id_factura = request.POST.get('id_factura')
        pedido.Total = request.POST.get('Total')
        pedido.Entregado = request.POST.get('Entregado')
        pedido.save()
        return redirect('Ver_pedidos')

    return render(request, 'actualizar_pedido.html', {'pedido': pedido})

@login_required
def borrar_pedido(request, id):
    pedido = Pedido.objects.get(id_factura=id)
    
    if request.method == 'POST':
        pedido.delete()
        return redirect('Ver_pedidos')

    return render(request, 'borrar_pedido.html', {'pedido': pedido})

@login_required
def actualizar_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    
    if request.method == 'POST':
        cliente.zona = request.POST.get('zona')
        cliente.nombre = request.POST.get('nombre')
        cliente.calle = request.POST.get('calle')
        cliente.razon_social = request.POST.get('razon_social')
        cliente.numero_cel = request.POST.get('numero_cel')
        cliente.email = request.POST.get('email')
        cliente.cuit = request.POST.get('cuit')
        cliente.save()
        return redirect('ver_clientes')

    return render(request, 'actualizar_cliente.html', {'cliente': cliente})

@login_required
def borrar_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')

    return render(request, 'borrar_cliente.html', {'cliente': cliente})

def iniciar_sesion(request):
    if request.method =='POST':
        formulario = AuthenticationForm(request,data = request.POST)
        if formulario.is_valid():
            info_dic = formulario.cleaned_data
            
            usuario = authenticate(username = info_dic["username"], password = info_dic["password"])

            if usuario is not None:

                login(request, usuario)

                return render(request,"Index_log.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"Index.html", {"mensaje":"ERROR EN EL INICIO DE SESION"})

    else:
        formulario = AuthenticationForm()    
        
    return render(request,'log_in.html',{"formu":formulario})

def cerrar_sesion(request):
    logout(request)
    return render(request,'Index.html')

def Registrarse (request):

    if request.method =="POST":
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            return render (request, "Index.html", {"mensaje":"Usuario creado correctamente"})
    else:
        formulario = UserCreationForm()

    return render (request,"registrarse.html", {"formu":formulario})