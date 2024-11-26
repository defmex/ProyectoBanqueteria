# Generated by Django 5.1.3 on 2024-11-26 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eventos', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
                ('id_evento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
                ('id_trabajador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.trabajador')),
            ],
        ),
    ]
