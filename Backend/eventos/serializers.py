from rest_framework import serializers
from .models import Banqueteria, Evento, Componente, Local

class BanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banqueteria
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'
