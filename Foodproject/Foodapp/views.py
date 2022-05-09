from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.
class FoodAPIView(APIView):
    serializer_class = FoodSerializer
    def get(self,request):
        allFoods = Food.objects.all().values()
        return Response({'List of Food items: ',allFoods})

    def post(self,request):
        serializer_obj = FoodSerializer(data=request.data)
        if serializer_obj.is_valid():
            Food.objects.create(id=serializer_obj.data.get('id'),
                                name=serializer_obj.data.get('name'),
                                price=serializer_obj.data.get('price'),
                                location=serializer_obj.data.get('location')
                                )

        addFood = Food.objects.all().filter(id=request.data['id']).values()
        return Response({'Food item added successfully: ',addFood})
