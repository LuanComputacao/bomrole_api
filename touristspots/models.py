from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)


class TouristSpot(models.Model):
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "%s (%s) [%s, %s]" % (self.name, self.latitude, self.longitude, self.category)

    class Meta:
        ordering = ['name']
