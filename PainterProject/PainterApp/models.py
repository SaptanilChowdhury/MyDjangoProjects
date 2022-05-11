from django.db import models

# Create your models here.
class Painter(models.Model):
    id = models.IntegerField(primary_key=True)
    painting_name = models.CharField(max_length=100)
    painter_name = models.CharField(max_length=50)


