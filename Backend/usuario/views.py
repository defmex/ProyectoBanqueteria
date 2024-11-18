from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from .models import Cliente, Trabajador
from .serializers import ClienteSerializer, TrabajadorSerializer
from django.http import JsonResponse
import json

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

class ComercialLogin(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        password = request.data.get('password')

        # Verifica que se proporcionen ambos campos
        if not nombre or not password:
            return Response({"error": "Nombre y contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca el comercial por el nombre
            Cliente = Cliente.objects.get(nombre=nombre)
            
            # Verifica la contraseña
            if Cliente.check_password(password):
                return Response({"success": "Autenticación exitosa"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Cliente.DoesNotExist:
            return Response({"error": "El comercial no existe"}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def get_comercial_id(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            password = data.get('password')
            
            # Busca el Comercial por nombre
            Cliente = Cliente.objects.get(nombre=nombre)
            
            # Verifica la contraseña
            if Cliente.check_password(password):
                return JsonResponse({'rut': Cliente.rut}, status=200)
            else:
                return JsonResponse({'error': 'Contraseña incorrecta'}, status=400)
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Comercial no encontrado'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Nombre y contraseña son requeridos'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

class ComercialLogin(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        password = request.data.get('password')

        # Verifica que se proporcionen ambos campos
        if not nombre or not password:
            return Response({"error": "Nombre y contraseña son requeridos"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca el comercial por el nombre
            Trabajador = Trabajador.objects.get(nombre=nombre)
            
            # Verifica la contraseña
            if Trabajador.check_password(password):
                return Response({"success": "Autenticación exitosa"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Trabajador.DoesNotExist:
            return Response({"error": "El comercial no existe"}, status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def get_comercial_id(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            password = data.get('password')
            
            # Busca el Comercial por nombre
            Trabajador = Trabajador.objects.get(nombre=nombre)
            
            # Verifica la contraseña
            if Trabajador.check_password(password):
                return JsonResponse({'rut': Trabajador.rut}, status=200)
            else:
                return JsonResponse({'error': 'Contraseña incorrecta'}, status=400)
        except Trabajador.DoesNotExist:
            return JsonResponse({'error': 'Comercial no encontrado'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Nombre y contraseña son requeridos'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
