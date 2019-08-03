from django.db import models

# Create your models here.


class Student(models.Model):
    name1 = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    schoolName = models.CharField(max_length=50)
    group = models.CharField(max_length=10)
    marks = models.CharField(max_length=10)
    stateRank = models.CharField(max_length=10)
    award = models.CharField(max_length=100)
    password = models.CharField(max_length=50)