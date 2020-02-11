from rest_framework import viewsets

from touristspots.models import FavoriteTouristSpot
from touristspots.serializers import FavoriteTouristSpotSerializer


class FavoriteTouristSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Favorite Tourist Spot Serializer to be viewed and edited
    """
    queryset = FavoriteTouristSpot.objects.all()
    serializer_class = FavoriteTouristSpotSerializer
