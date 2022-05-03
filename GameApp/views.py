from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class GameApiView(APIView):
    serializer_class = GameSerializer
    def get(self,request):
        allGames = Game.objects.all().values()
        return Response({"Message":"List of games","Games List":allGames})

    def post(self,request):
        print("Request data is: ",request.data)
        serializer_obj = GameSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Game.objects.create(game_id=serializer_obj.data.get("game_id"),
                                game_name=serializer_obj.data.get("game_name"),
                                developer_name=serializer_obj.data.get("developer_name")
                                )

        games = Game.objects.all().filter(id=request.data['game_id']).values()
        return Response({"Message":"New Game Added!", "Game":games})

