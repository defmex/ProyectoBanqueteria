from django.shortcuts import render
from rest_framework import generics

from .models import Reserva
from .serializers import ReservaSerializer
# Create your views here.
class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
    def perform_create(self, serializer):
        reserva = serializer.save()
        reserva.calcularTotal()

class ReservaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer