from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class LanguageAPIView(APIView):
    serializer_class = Language_Serializer
    def get(self,request):
        languages = Language.objects.all().values()
        return Response({'Message:','List of Programming languages: ''Programming languages: ',languages})

    def post(self,request):
        serializer_obj = Language_Serializer(data=request.data)
        if(serializer_obj.is_valid()):


            Language.objects.create(id=serializer_obj.data.get("id"),
                                    name=serializer_obj.data.get("name"),
                                    developer=serializer_obj.data.get("developer")
                                    )

        langs = Language.objects.all().filter(id=request.data['id']).values()
        return Response({'Message:','New Programming language added: ',langs})


