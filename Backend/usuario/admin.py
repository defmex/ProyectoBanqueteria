from django.contrib import admin
from .models import Cliente, Trabajador

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido1', 'apellido2', 'fecha_nacimiento', 'nickname', 'ciudad', 'telefono', 'correo', 'password')


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido1', 'apellido2', 'fecha_nacimiento', 'nickname', 'ciudad', 'telefono', 'correo', 'password', 'rango')
