from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=60)
    course = models.CharField(max_length=20)
    stream = models.CharField(max_length=20)
