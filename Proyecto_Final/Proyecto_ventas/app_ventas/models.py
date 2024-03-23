from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    numero_cel = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    email = models.EmailField()
    cuit = models.BigIntegerField()

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BigIntegerField()
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

class Pedido(models.Model):
    id_factura = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Entregado=models.BooleanField()
    