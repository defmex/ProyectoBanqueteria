from django.db import models

# Create your models here.
class Informe(models.Model):
    salones_arrendados = models.IntegerField()
    banqueteria_vendidas = models.IntegerField()
    mes = models.CharField(max_length=100)
    total_mensual = models.IntegerField()
    cancelaciones = models.CharField(max_length=100)