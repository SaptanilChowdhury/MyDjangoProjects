from rest_framework import serializers


class Language_Serializer(serializers.Serializer):
    id = serializers.IntegerField(label="Enter programming language id: ")
    name = serializers.CharField(label="Enter programming language name: ")
    developer = serializers.CharField(label="Enter developer name: ")

