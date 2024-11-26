from django.db import models
from eventos.models import Evento
from usuario.models import Trabajador

# Create your models here.
class Reserva(models.Model):
    total = models.IntegerField()
    estado = models.CharField(max_length=100)
    id_evento = models.OneToOneField(Evento, on_delete=models.CASCADE, null=False, blank=False)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id_evento , self.estado, self.total}"