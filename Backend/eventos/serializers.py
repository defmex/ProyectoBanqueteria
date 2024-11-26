from rest_framework import serializers
from .models import Banqueteria, Evento, Componente, Local, EventoComponente

class BanqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banqueteria
        fields = '__all__'

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
class EventoSerializer(serializers.ModelSerializer):
    detalles = EventoComponenteSerializer(many=True, write_only=True)
    componentes = ComponenteSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ['id', 'num_personas', 'detalles', 'fecha_evento', 'cliente', 'banqueteria', 'local', 'componentes']

    def create(self, validated_data):
        print("Datos validados:", validated_data)
        # Extraemos los detalles del evento
        detalles_data = validated_data.pop('detalles')
        banqueteria_data = validated_data.pop('banqueteria')
        evento = Evento.objects.create(**validated_data)
        
        # Añadir banqueteria al evento
        for banqueteria_id in banqueteria_data:
            evento.banqueteria.add(banqueteria_id)
        
        # Crear los componentes del evento
        for detalle_data in detalles_data:
            componente_id = detalle_data['componente'].id
            componente = Componente.objects.get(id=componente_id)
            EventoComponente.objects.create(
                evento=evento,
                componente=componente,
                cantidad=detalle_data['cantidad']
            )

        return evento