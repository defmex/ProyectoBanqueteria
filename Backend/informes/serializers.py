from rest_framework import serializers
from .models import Informe

#To convert your models into JSON for the API

class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = '__all__'