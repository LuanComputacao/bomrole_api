from rest_framework import viewsets, permissions

from touristspots.models import TouristSpotUpvote
from touristspots.serializers import TouristSpotUpvoteSerializer


class TouristSpotUpvotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spot Upvotes to be viewed and edited
    """
    queryset = TouristSpotUpvote.objects.all()
    serializer_class = TouristSpotUpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]