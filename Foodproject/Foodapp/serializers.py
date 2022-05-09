from rest_framework import serializers

class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Food Id: ")
    name = serializers.CharField(label="Enter Food name: ")
    price = serializers.IntegerField(label="Enter price of food: ")
    location = serializers.CharField(label="Enter location of food: ")
