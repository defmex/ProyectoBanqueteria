from rest_framework import serializers
from .models import Banqueteria, Evento, ComponenteBanqueteria, Local

class BanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banqueteria
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ComponenteBanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteBanqueteria
        fields = '__all__'

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'
