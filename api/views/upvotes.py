from rest_framework import viewsets, permissions

from api.models import TouristSpotUpvote
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TouristSpotUpvoteSerializer


class TouristSpotUpvotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourist Spot Upvotes to be viewed and edited
    """
    queryset = TouristSpotUpvote.objects.all()
    serializer_class = TouristSpotUpvoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
