from rest_framework import viewsets, permissions

from api.models import TouristSpotComments
from api.serializers import TouristSpotCommentSerializer


class TouristSpotCommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spot Comments to be viewed and edited
    """
    queryset = TouristSpotComments.objects.all()
    serializer_class = TouristSpotCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
