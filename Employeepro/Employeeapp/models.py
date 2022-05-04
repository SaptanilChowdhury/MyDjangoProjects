from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id = models.IntegerField()
    Employee_name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Salary = models.IntegerField()