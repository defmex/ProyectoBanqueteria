from django.db import models
from usuario.models import Cliente

# Create your models here.
class ComponenteBanqueteria(models.Model):
    tipo = models.CharField(max_length=100)
    costo = models.IntegerField()
    
class Banqueteria(models.Model):
    tipo = models.CharField(max_length=100)
    costo = models.IntegerField()
    componentes = models.ManyToManyField(ComponenteBanqueteria)

class Local(models.Model):
    nombre_local = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.IntegerField()

class Evento(models.Model):
    num_personas = models.IntegerField()
    fecha_evento = models.DateField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)   
    id_banqueteria = models.ForeignKey(Banqueteria, on_delete=models.CASCADE, null=True, blank=True)
    id_local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_cliente}"