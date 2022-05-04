from .models import Car
from .import views
from .serializers import CarSerializer
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('cars',views.CarAPIView)

urlpatterns = [
    path('',include(router.urls))
]