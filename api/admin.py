from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from api.models import TouristSpotCategory, TouristSpot, TouristSpotUpvote, TouristSpotsPictures, \
    TouristSpotComments


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class TouristSpotAdmin(OSMGeoAdmin):
    list_display = ('name', 'category', 'upvotes_count', 'point', 'registered_by', 'created_at')
    fields = ('name', 'registered_by', 'category', 'point', 'deleted_at')
    default_zoom = -4

    def upvotes_count(self, obj):
        return obj.upvotes.count()

    upvotes_count.short_description = 'Upvotes'


class TouristSpotUpvoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'tourist_spot')


class TouristSpotsPicturesAdmin(admin.ModelAdmin):
    list_display = ('user', 'tourist_spot')


class TouristSpotCommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')


admin.site.register(TouristSpotCategory, CategoryAdmin)
admin.site.register(TouristSpot, TouristSpotAdmin)
admin.site.register(TouristSpotUpvote, TouristSpotUpvoteAdmin)
admin.site.register(TouristSpotsPictures, TouristSpotsPicturesAdmin)
admin.site.register(TouristSpotComments, TouristSpotCommentsAdmin)
