from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.contrib.gis.db.models import PolygonField, PointField
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    now = datetime.today()
    return 'user_{0}/{1}/{2}/{3}/{4}'.format(instance.user.id, now.year, now.month, now.day, filename)


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

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
    point = PointField(null=True, blank=True)
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='tourist_spots')
    category = models.ForeignKey(TouristSpotCategory, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = _('Tourist Spot')
        verbose_name_plural = _('Toutist Spots')
        ordering = ['name']

    def __str__(self):
        return "%s (%s) [%s]" % (self.name, self.category, self.point)


class TouristSpotUpvote(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, blank=False, default=None,
                                     related_name='upvotes')

    class Meta:
        verbose_name = _('Tourist Spot Upvote')
        verbose_name_plural = _('Tourist Spot Upvotes')


class TouristSpotComments(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=255, null=False, blank=False, default='')
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, blank=False, related_name='comments')

    class Meta:
        verbose_name = _('Tourist Spot Comment')
        verbose_name_plural = _('Tourist Spot Comments')


class FavoriteTouristSpot(TimeStamps):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Favorite Tourist Spot')
        verbose_name_plural = _('Favorite Tourist Spots')


class TouristSpotsPictures(TimeStamps):
    _directory = 'tourist_spot'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tourist_spots_pictures')
    tourist_spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, null=False, related_name='pictures')
    picture = models.ImageField(upload_to=user_directory_path, null=False, blank=False)

    class Meta:
        verbose_name = _('Tourist Spot Image')
        verbose_name_plural = _('Tourist Spot Images')
