from django.contrib.auth.models import User, Group
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from api.models import TouristSpot, TouristSpotCategory, TouristSpotUpvote, TouristSpotComments, \
    FavoriteTouristSpot, TouristSpotsPictures


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'password'
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]


class TouristSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpot
        fields = [
            'url',
            'name',
            'category',
            'point',
            'upvotes_count',
        ]

    point = PointField()

    upvotes_count = serializers.SerializerMethodField()

    def get_upvotes_count(self, obj):
        return obj.upvotes.count()


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotCategory
        fields = [
            'url',
            'name'
        ]


class TouristSpotUpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotUpvote
        fields = [
            'tourist_spot'
        ]


class TouristSpotCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotComments
        fields = [
            'url',
            'user',
            'text',
            'tourist_spot'
        ]


class FavoriteTouristSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteTouristSpot
        fields = [
            'url',
            'user',
            'tourist_spot',
        ]


class TouristSpotsPicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotsPictures
        fields = [
            'url',
            'user',
            'tourist_spot',
            'picture'
        ]
