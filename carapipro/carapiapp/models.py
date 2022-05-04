from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=50)
    car_price = models.IntegerField()

