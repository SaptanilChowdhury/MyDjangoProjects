from django.db import models

# Create your models here.
class Cricketer(models.Model):
    cricketer_name = models.CharField(max_length=100)
    cricketer_age = models.IntegerField()
    runs = models.IntegerField()
    batting_avg = models.IntegerField()