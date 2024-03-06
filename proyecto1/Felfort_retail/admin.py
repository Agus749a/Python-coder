from django.contrib import admin
from .models import clientes
from .models import productos

admin.site.register(clientes)
admin.site.register(productos)