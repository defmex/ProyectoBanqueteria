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
    def post(self, request):

        def obtener_mes_de_fecha(fecha_str):
            # Convertir la cadena de fecha a un objeto datetime
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            # Obtener el mes de la fecha
            mes = fecha.month
            return mes

        mesSeleccionado = int(request.data.get("mes")) #se puede cambiar el mes seleccionado
        reservas = Reserva.objects.all()
        cantidadBanqueteria = 0
        cantidadLocal = 0
        cantidadCancelaciones = 0
        totalMensual = 0


        for reserva in reservas:
            mes = obtener_mes_de_fecha(str(reserva.id_evento.fecha_evento))
            print(reserva.id_evento.fecha_evento)
            print(mes)
            if mes == mesSeleccionado:
                if reserva.estado == False:
                    cantidadCancelaciones += 1
                    
                else:    
                    if reserva.id_evento.banqueteria.exists():
                        cantidadBanqueteria += reserva.id_evento.banqueteria.count()
                    if reserva.id_evento.local:
                        cantidadLocal += 1
                    totalMensual += reserva.total
        
        informe = Informe.objects.create(
            mes=mesSeleccionado,
            total_mensual=totalMensual,
            salones_arrendados=cantidadLocal,
            banqueteria_vendidas=cantidadBanqueteria,
            cancelaciones=cantidadCancelaciones
        )

        serializer = InformeSerializer(informe)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


    
    
        