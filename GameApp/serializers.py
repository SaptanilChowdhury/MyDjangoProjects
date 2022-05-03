from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    game_id = serializers.IntegerField(label="Enter Game Id: ")
    game_name = serializers.CharField(label="Enter Game name: ")
    developer_name = serializers.CharField(label="Enter developer name: ")