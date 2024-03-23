# Generated by Django 5.0.3 on 2024-03-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ventas', '0005_remove_pedido_producto_pedido_remove_pedido_subtotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='total',
            new_name='Total',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='cliente_pedido',
            new_name='id_cliente',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='id_pedido',
            new_name='id_factura',
        ),
        migrations.AddField(
            model_name='pedido',
            name='Entregado',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
