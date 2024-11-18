from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .models import Cliente, Trabajador
from .serializers import ClienteSerializer, TrabajadorSerializer

# Create your views here.

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class TrabajadorListCreate(generics.ListCreateAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

class TrabajadorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer