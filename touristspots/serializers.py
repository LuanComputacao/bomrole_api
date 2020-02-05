from django.contrib.auth.models import User, Group
from rest_framework import serializers

from touristspots.models import TouristSpot, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TouristSpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TouristSpot
        fields = [
            'url',
            'latitude',
            'longitude',
            'name',
            'category',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name']
