from rest_framework import serializers
from .models import Reserva

#To convert your models into JSON for the API

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


