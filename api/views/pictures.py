from rest_framework import viewsets

from api.models import TouristSpotsPictures
from api.serializers import TouristSpotsPicturesSerializer


class TouristSpotsPicturesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spot Pictures to be viewed and edited
    """
    queryset = TouristSpotsPictures.objects.all()
    serializer_class = TouristSpotsPicturesSerializer
