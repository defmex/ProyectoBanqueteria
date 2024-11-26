from rest_framework import serializers
from .models import Banqueteria, Evento, Componente, Local, EventoComponente, EventoBanqueteria

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class EventoComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoComponente
        fields = ['componente', 'cantidad']

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'


class BanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banqueteria
        fields = '__all__'

class EventoBanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoBanqueteria
        fields = ['banqueteria', 'cantidad']


class EventoSerializer(serializers.ModelSerializer):
    detallesComponente = EventoComponenteSerializer(many=True, write_only=True)
    componentes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    detallesBanqueteria = EventoBanqueteriaSerializer(many=True, write_only=True)
    banqueteria = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ['id', 'num_personas', 'detallesComponente', 'detallesBanqueteria', 'fecha_evento', 'cliente', 'local', 'banqueteria', 'componentes']

    def create(self, validated_data):
        print("Datos validados:", validated_data)
        # Extraemos los detalles del evento
        detallesComponente_data = validated_data.pop('detallesComponente')
        detallesBanqueteria_data = validated_data.pop('detallesBanqueteria')
        evento = Evento.objects.create(**validated_data)
        
        # Crear los componentes del evento
        for detalle_data in detallesBanqueteria_data:
            banqueteria_id = detalle_data['banqueteria'].id
            banqueteria = Banqueteria.objects.get(id=banqueteria_id)
            EventoBanqueteria.objects.create(
                evento=evento,
                banqueteria=banqueteria,
                cantidad=detalle_data['cantidad']
            )
        for detalle_data in detallesComponente_data:
            componente_id = detalle_data['componente'].id
            componente = Componente.objects.get(id=componente_id)
            EventoComponente.objects.create(
                evento=evento,
                componente=componente,
                cantidad=detalle_data['cantidad']
            )

        # Crear los detalles de banqueteria del evento

        return evento
