# Generated by Django 5.1.3 on 2024-11-26 07:32

from django.db import migrations

def cargar_datos(apps, schema_editor):
    componente = apps.get_model('eventos', 'componente')  # Ajusta nombre_app y NombreModelo
    componente.objects.create(tipo='silla', costo='4000', descripcion='Silla ergonomica para largas horas de evento', link_img='https://eventosmarietta.com/img/productos/Silla_01.png')  # Agrega los datos que necesites
    componente.objects.create(tipo='mesa', costo='5000', descripcion='Mesa para cuatros personas para largas horas de eventos', link_img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBUiHNx6gqXX-LonT2Y2L7hpkpx8wjx04kmg&s')

    banqueteria = apps.get_model('eventos', 'banqueteria')  # Ajusta nombre_app y NombreModelo
    banqueteria.objects.create(tipo='Tortas para matrimonio', costo='30000', descripcion='Ricas tortas de manjar para 20 personas', link_img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYdI6lvx5WDlYkKCgY5Ptjt_v2Rbm9XjvtTQ&s')  # Agrega los datos que necesites
    banqueteria.objects.create(tipo='Partes', costo='5000', descripcion='Servicios para partes en pleno evento', link_img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuypOEVPYvgo--C7MBuli8KI7YjH4HVCQoHw&s')  # Agrega los datos que necesites

    local = apps.get_model('eventos', 'local')  # Ajusta nombre_app y NombreModelo
    local.objects.create(nombre_local='Gran Manzano', ciudad='Viña del Mar', capacidad='400', precio='100000', descripcion='Amplio salon con capacidad para 400 personas ubicada en Viña del Mar', link_img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3y2-IGY2O9mJP7agOM6yr3RGADK27WP0dnQ&s')  # Agrega los datos que necesites 
    local.objects.create(nombre_local='El Quisco', ciudad='El Quisco', capacidad='300', precio='80000', descripcion='Amplio salon con capacidad para 300 personas ubicada en el Quisco', link_img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaSAl-tG3eROVWCsWBskap3h0y0P6CTjyuvA&s')  # Agrega los datos que necesites



class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cargar_datos),
    ]
