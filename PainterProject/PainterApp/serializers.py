from rest_framework import serializers

class PainterSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter painting id: ")
    painting_name = serializers.CharField(label="Enter painting name: ")
    painter_name = serializers.CharField(label="Enter painter name: ")

