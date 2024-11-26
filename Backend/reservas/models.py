from django.db import models
from eventos.models import Evento
from usuario.models import Trabajador

# Create your models here.
class Reserva(models.Model):
    total = models.IntegerField(default=0)
    estado = models.BooleanField(max_length=100)
    id_evento = models.OneToOneField(Evento, on_delete=models.CASCADE, null=False, blank=False)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_evento , self.estado, self.total}"
    
    def calcularTotal(self):
        total = 0
        for evento_banqueteria in self.id_evento.eventobanqueteria_set.all():
            banqueteria = evento_banqueteria.banqueteria
            cantidad = evento_banqueteria.cantidad
            total += banqueteria.costo * cantidad
        for evento_componente in self.id_evento.eventocomponente_set.all():
            componente = evento_componente.componente
            cantidad = evento_componente.cantidad
            total += componente.costo * cantidad
        local = self.id_evento.local
        total += local.precio
        
        self.total = total
        self.save()