from rest_framework import serializers
from .models import Pago

#To convert your models into JSON for the API

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

