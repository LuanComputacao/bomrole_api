from django.contrib import admin

# Register your models here.
from touristspots.models import TouristSpotCategory, TouristSpot, TouristSpotUpvote


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'upvotes_count', 'latitude', 'longitude', 'registered_by', 'created_at')

    def upvotes_count(self, obj):
        return obj.upvotes.count()

    upvotes_count.short_description = 'Upvotes'



class TouristSpotUpvoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'tourist_spot')


admin.site.register(TouristSpotCategory, CategoryAdmin)
admin.site.register(TouristSpot, TouristSpotAdmin)
admin.site.register(TouristSpotUpvote, TouristSpotUpvoteAdmin)
