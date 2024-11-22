from django.shortcuts import render
from rest_framework import generics

from .models import Pago
from .serializers import PagoSerializer
# Create your views here.
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer