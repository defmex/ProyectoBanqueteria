# Generated by Django 5.1.3 on 2024-11-26 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='componenetes',
            new_name='componentes',
        ),
        migrations.RenameField(
            model_name='eventocomponente',
            old_name='id_componente',
            new_name='componente',
        ),
        migrations.RenameField(
            model_name='eventocomponente',
            old_name='id_evento',
            new_name='evento',
        ),
    ]
