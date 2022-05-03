from rest_framework import serializers
from .models import Cricketer

class CricketerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketer
        fields = ('cricketer_name','cricketer_age','runs','batting_avg')