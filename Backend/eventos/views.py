from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json


from .serializers import BanqueteriaSerializer, LocalSerializer, ComponenteBanqueteriaSerializer, EventoSerializer
from .models import Banqueteria, Local, ComponenteBanqueteria, Evento


class EventoListCreate(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class LocalListCreate(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class BanqueteriaListCreate(generics.ListCreateAPIView):
    queryset = Banqueteria.objects.all()
    serializer_class = BanqueteriaSerializer

class BanqueteriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banqueteria.objects.all()
    serializer_class = BanqueteriaSerializer

class ComponenteBanqueteriaListCreate(generics.ListCreateAPIView):
    queryset = ComponenteBanqueteria.objects.all()
    serializer_class = ComponenteBanqueteriaSerializer

class ComponenteBanqueteriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComponenteBanqueteria.objects.all()
    serializer_class = ComponenteBanqueteriaSerializer

