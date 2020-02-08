import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from touristspots.models import TouristSpot, Category, TouristSpotUpvote
from touristspots.serializers import UserSerializer, GroupSerializer, TouristSpotSerializer, CategorySerializer, \
    TouristSpotUpvoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TouristSpotFilter(django_filters.FilterSet):
    """
    Filter to be applied to the Tourist Spot View Set
    """

    class Meta:
        model = TouristSpot
        fields = {
            'name': ['icontains']
        }


class TouristSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spots to be viewed and edited
    """
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filterset_class = TouristSpotFilter

    def perform_create(self, serializer):
        serializer.save(registered_by=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed and edited
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class TouristSpotUpvoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spot Upvotes to be viewed and edited
    """
    queryset = TouristSpotUpvote.objects.all()
    serializer_class = TouristSpotUpvoteSerializer
