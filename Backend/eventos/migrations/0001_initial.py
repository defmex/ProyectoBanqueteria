# Generated by Django 5.1.3 on 2024-11-26 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banqueteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('costo', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('link_img', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('costo', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('link_img', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_local', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('capacidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('link_img', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_personas', models.IntegerField()),
                ('fecha_evento', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='EventoBanqueteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('banqueteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.banqueteria')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='banqueteria',
            field=models.ManyToManyField(through='eventos.EventoBanqueteria', to='eventos.banqueteria'),
        ),
        migrations.CreateModel(
            name='EventoComponente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.componente')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='componentes',
            field=models.ManyToManyField(through='eventos.EventoComponente', to='eventos.componente'),
        ),
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.local'),
        ),
    ]
