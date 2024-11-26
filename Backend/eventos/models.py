from django.db import models
from usuario.models import Cliente

# Create your models here.
class Componente(models.Model):
    tipo = models.CharField(max_length=100)
    costo = models.IntegerField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    link_img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo}"

class Banqueteria(models.Model):
    tipo = models.CharField(max_length=100)
    costo = models.IntegerField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    link_img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo}"

class Local(models.Model):
    nombre_local = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    link_img = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_local}"
    
class EventoComponente(models.Model):
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    componente = models.ForeignKey('Componente', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.evento}"
    
class Evento(models.Model):
    componentes = models.ManyToManyField(Componente, through='EventoComponente')
    num_personas = models.IntegerField()
    fecha_evento = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    banqueteria = models.ManyToManyField(Banqueteria)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.cliente}"