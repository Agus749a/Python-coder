# Generated by Django 5.0.2 on 2024-02-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Felfort_retail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('calle', models.TextField()),
                ('razon_social', models.TextField()),
                ('telefono', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('cuit', models.CharField(max_length=17)),
            ],
        ),
    ]
