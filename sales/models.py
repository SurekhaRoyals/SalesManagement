from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE)
    joining_date = models.DateField()
    names = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    education = models.CharField(max_length=20)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.name
