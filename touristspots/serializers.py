from django.contrib.auth.models import User, Group
from rest_framework import serializers

from touristspots.models import TouristSpot, Category, TouristSpotUpvote


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
            'latitude',
            'longitude',
            'registered_by',
            'url'
        ]

    upvotes_count = serializers.SerializerMethodField()

    def get_upvotes_count(self, obj):
        return obj.upvotes.count()


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']


class TouristSpotUpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpotUpvote
        fields = [
            'user',
            'tourist_spot'
        ]
