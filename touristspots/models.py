from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class TouristSpotCategory(TimeStamps):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return "%s" % self.name


class TouristSpot(TimeStamps):
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='tourist_spots')
    category = models.ForeignKey(TouristSpotCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = _('Tourist Spot')
        verbose_name_plural = _('Toutist Spots')
        ordering = ['name']

    def __str__(self):
        return "%s (%s) [%s,%s]" % (self.name, self.category, self.latitude, self.longitude)


class TouristSpotUpvote(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, blank=False, default=None,
                                     related_name='upvotes')

    class Meta:
        verbose_name = _('Tourist Spot Upvote')
        verbose_name_plural = _('Tourist Spot Upvotes')


class TouristSpotComments(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=255, null=False, blank=False, default='')

    class Meta:
        verbose_name = _('Tourist Spot Comment')
        verbose_name_plural = _('Tourist Spot Comments')


class FavoriteTouristSpot(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Favorite Tourist Spot')
        verbose_name_plural = _('Favorite Tourist Spots')


