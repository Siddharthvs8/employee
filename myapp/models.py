from django.db import models
class Employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_age=models.IntegerField(default=0)
    employee_contact=models.IntegerField(default=0)
    employee_email=models.CharField(max_length=50)


# Create your models here.
