from django.db import models

# Create your models here.

class Weather(models.Model):
    digit = models.CharField(max_length=10)
