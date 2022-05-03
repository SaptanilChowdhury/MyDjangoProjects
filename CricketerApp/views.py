from django.shortcuts import render
from rest_framework import viewsets
from .models import Cricketer
from .serializers import CricketerSerializer
# Create your views here.
class CricketerView(viewsets.ModelViewSet):
    queryset = Cricketer.objects.all()
    serializer_class = CricketerSerializer