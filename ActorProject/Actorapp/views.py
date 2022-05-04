from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor
from .serializers import ActorSerializer

# Create your views here.
class ActorView(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
