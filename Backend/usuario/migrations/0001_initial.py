# Generated by Django 5.1.3 on 2024-11-18 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('nickname', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(auto_now=True)),
                ('nickname', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('rango', models.IntegerField()),
            ],
        ),
    ]
