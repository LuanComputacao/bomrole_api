from rest_framework import viewsets

from api.models import FavoriteTouristSpot
from api.serializers import FavoriteTouristSpotSerializer


class FavoriteTouristSpotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Favorite Tourist Spot Serializer to be viewed and edited
    """
    queryset = FavoriteTouristSpot.objects.all()
    serializer_class = FavoriteTouristSpotSerializer
