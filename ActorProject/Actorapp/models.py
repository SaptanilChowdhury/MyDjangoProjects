from django.db import models

# Create your models here.
class Actor(models.Model):
    actor_name = models.CharField(max_length=100)
    actor_age = models.IntegerField()
    movie_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=70)

    