from django.contrib.auth.models import User, Group
# Create your views here.
from rest_framework import viewsets

from touristspots.models import TouristSpot, Category
from touristspots.serializers import UserSerializer, GroupSerializer, TouristSpotSerializer, CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TouristSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spots to be viewed and edited
    """
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed and edited
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
