from django.db import models
from reservas.models import Reserva
# Create your models here.
class Pago(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=False, blank=False)
    monto = models.IntegerField()
    metodo_pago = models.CharField(max_length=100)
    fechas_pago =  models.DateField()