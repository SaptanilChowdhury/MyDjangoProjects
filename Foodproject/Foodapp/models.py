from django.db import models

# Create your models here.
class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    location = models.CharField(max_length=100)
