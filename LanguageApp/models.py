from django.db import models

# Create your models here.
class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)


