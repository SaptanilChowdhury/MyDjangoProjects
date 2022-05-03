from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    product_price = models.IntegerField()
    product_brand = models.CharField(max_length=150)