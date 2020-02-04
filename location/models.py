from django.db import models


# Create your models here.

class TouristSpot(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
