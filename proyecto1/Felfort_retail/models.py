from django.db import models

# Create your models here.

class productos(models.Model):
    id_producto= models.IntegerField()
    Product_name = models.CharField(max_length=50)
    stock = models.IntegerField()
    Product_descripcion = models.TextField()
    Precio = models.FloatField()


class clientes(models.Model):
    Nombre = models.CharField(max_length=50)
    calle = models.TextField()
    razon_social = models.TextField()
    telefono = models.TextField()
    email = models.EmailField()
    cuit= models.CharField(max_length=17)

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    productos = models.ManyToManyField(productos, through='PedidoProducto')

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    