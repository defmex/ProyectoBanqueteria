from django.shortcuts import render
from rest_framework import generics

from .models import Informe
from .serializers import InformeSerializer
# Create your views here.
class InformeListCreate(generics.ListCreateAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer

class InformeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer