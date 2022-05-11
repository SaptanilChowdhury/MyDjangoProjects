from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class PainterAPIView(APIView):
    def get(self,request):
        allPainters = Painter.objects.all().values()
        return Response({'List of Painters and Painting',allPainters})

    def post(self,request):
        serializer_obj = PainterSerializer(data=request.data)
        if serializer_obj.is_valid():
            Painter.objects.create(id=serializer_obj.data.get('id'),
                                   painting_name=serializer_obj.data.get('painting_name'),
                                   painter_name=serializer_obj.data.get('painter_name')
                                   )

        addPainter = Painter.objects.all().filter(id=request.data['id']).values()
        return Response({'New Painter and Painting added',addPainter})

