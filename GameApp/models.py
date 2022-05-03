from django.db import models



# Create your models here.
class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=200)
    developer_name = models.CharField(max_length=200)
