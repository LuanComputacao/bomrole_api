from django.contrib.auth.models import User, Group
from rest_framework import serializers

from touristspots.models import TouristSpot, TouristSpotCategory, TouristSpotUpvote, TouristSpotComments, \
    FavoriteTouristSpot, TouristSpotsPictures


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'tourist_spots'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TouristSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpot
        fields = [
            'name',
            'category',
            'upvotes_count',
            'registered_by',
            'url'
        ]

    
    upvotes_count = serializers.SerializerMethodField()

    def get_upvotes_count(self, obj):
        return obj.upvotes.count()


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotCategory
        fields = ['url', 'name']


class TouristSpotUpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotUpvote
        fields = [
            'user',
            'tourist_spot'
        ]


class TouristSpotCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotComments
        fields = [
            'user',
            'text',
            'url'
        ]


class FavoriteTouristSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteTouristSpot
        fields = [
            'user',
            'tourist_spot',
            'url'
        ]


class TouristSpotsPicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotsPictures
        fields = [
            'user',
            'tourist_spot',
            'picture'
        ]
