from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.db.models.functions import ExtractMonth


from reservas.models import Reserva
from .models import Informe
from .serializers import InformeSerializer
# Create your views here.
class InformeListCreate(generics.ListCreateAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer

class InformeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Informe.objects.all()
    serializer_class = InformeSerializer

class InformeReserva(APIView):
    def get(self, request):

        def obtener_mes_de_fecha(fecha_str):
            # Convertir la cadena de fecha a un objeto datetime
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            # Obtener el mes de la fecha
            mes = fecha.month
            return mes

        mesSeleccionado = 11 #se puede cambiar el mes seleccionado
        reservas = Reserva.objects.all()
        cantidad_reservas = reservas.count()
        cantidadBanqueteria = 0
        cantidadLocal = 0
        totalMensual = 0

        for reserva in reservas:
            mes = obtener_mes_de_fecha(str(reserva.id_evento.fecha_evento))
            if mes == mesSeleccionado:
                banqueteriaPrecio = 0
                localPrecio = 0
                if reserva.id_evento.id_banqueteria != None:
                    cantidadBanqueteria += 1
                if reserva.id_evento.id_local != None:
                    cantidadLocal += 1
                if reserva.id_evento.id_banqueteria != None:
                    banqueteriaPrecio = int(reserva.id_evento.id_banqueteria.costo)
                if reserva.id_evento.id_local != None:
                    localPrecio = int(reserva.id_evento.id_local.precio)
                total = banqueteriaPrecio + localPrecio 
                totalMensual += total
        
        print(totalMensual)


        return Response({
            'cantidad_reservas': cantidad_reservas,
            'datos_reservas': mes,
        }, status=status.HTTP_200_OK)
        


    
    
        