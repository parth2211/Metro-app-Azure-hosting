from django.db import models

# Create your models here.
class Analytics(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    source = models.CharField(max_length=40)
    destination = models.CharField(max_length=40)

class Count(models.Model):
    add = models.CharField(max_length=40)
    count = models.IntegerField(default=10)
    