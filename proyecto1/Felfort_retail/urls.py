"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import reverse
from django.urls import path
from proyecto1.views import *
from Felfort_retail.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/', index, name='index'),
    path('Generar_clientes.html/', Generar_cliente, name='Generar_cliente'),
    path('Clientes.html/', ver_clientes, name='ver_clientes'),
    path('agregar_producto.html/', agregar_producto, name='agregar_producto'),
    path('buscar_cliente.html/',venta, name='venta'),
    path('buscar_cliente.html/detalle_venta.html',venta, name='venta')
]