from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import viewsets

# Create your views here.
class CarAPIView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

