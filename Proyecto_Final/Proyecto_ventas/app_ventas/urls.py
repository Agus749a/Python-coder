"""Felfort_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto_ventas.views import * 
from app_ventas.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Index/', Index, name = 'index' ),
    path('Agregar_clientes/', Agregar_clientes, name= 'Agregar_clientes'),
    path('Agregar_productos/', Agregar_productos, name='Agregar_productos'),
    path('Ver_clientes/', ver_clientes, name= 'ver_clientes'),
    path('Cargar_venta/', Cargar_venta, name= 'Cargar_venta'),
    path('Ver_pedidos/', Ver_pedidos, name= 'Ver_pedidos'),
    path('actualizar_pedido/<int:id>/', actualizar_pedido, name= 'actualizar_pedido'),
    path('borrar_pedido/<int:id>/', borrar_pedido, name= 'borrar_pedido'),
    path('actualizar_cliente/<int:id>/', actualizar_cliente, name= 'actualizar_cliente'),
    path('borrar_cliente/<int:id>/', borrar_cliente, name= 'borrar_cliente'),
    path('iniciar_sesion/', iniciar_sesion, name= 'iniciar_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name= 'cerrar_sesion'),
    path('Registrarse/', Registrarse, name= 'Registrarse')
]
